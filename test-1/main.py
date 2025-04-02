import os
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import zipfile
from typing import List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("web_scraping.log"),
        logging.StreamHandler(),
    ],
)


class ANSScraper:
    def __init__(self, base_url: str, target_names: Optional[List[str]] = None, output_dir: str = "downloads"):
        """
        Inicializa o scraper com a URL base e diretório de saída.

        :param base_url: URL base do site a ser raspado.
        :param output_dir: Diretório onde os arquivos serão salvos.
        """
        self.base_url = base_url
        self.target_names = target_names
        self.output_dir = output_dir
        self.session = requests.Session()

        # Cria o diretório de saída se não existir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def compress_files(self, filepaths: List[str], output_filename: str = "anexos.zip") -> str:
        """
        Compacta os arquivos baixados em um único arquivo ZIP.

        :param filepaths: Lista de caminhos dos arquivos a serem compactados.
        :param output_filename: Nome do arquivo ZIP de saída.
        :return: Caminho do arquivo ZIP gerado.
        """
        output_path = os.path.join(self.output_dir, output_filename)

        if os.path.exists(output_path):
            logging.warning(f"[Compressão] O arquivo ZIP '{output_path}' já existe e será sobrescrito.")

        logging.info(f"[Compressão] Iniciando compactação de {len(filepaths)} arquivos em '{output_path}'...")

        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for filepath in filepaths:
                zipf.write(filepath, os.path.basename(filepath))
                logging.debug(f"[Compressão] Arquivo '{filepath}' adicionado ao ZIP.")

        logging.info(f"[Compressão] Compactação concluída com sucesso. Arquivo gerado: '{output_path}'.")

        return output_path

    def download_file(self, url: str) -> str:
        """
        Faz o download de um arquivo e o salva no diretório especificado.

        :param url: URL do arquivo a ser baixado.
        :return: Caminho do arquivo salvo.
        """
        filename = os.path.basename(url)
        file_path = os.path.join(self.output_dir, filename)

        # Verifica se o arquivo já existe
        if os.path.exists(file_path):
            logging.info(f"[Download] O arquivo '{filename}' já existe no diretório. Pulando download.")
            return file_path

        content = self.get_page_content(url)

        with open(file_path, "wb") as file:
            file.write(content)

        logging.info(f"[Download] O arquivo '{filename}' foi baixado com sucesso e salvo em '{file_path}'.")

        return file_path

    def find_pdf_links(self, content: bytes) -> List[Tuple[str, str]]:
        """
        Encontra os links dos Anexos I e II na página a partir do conteúdo HTML.

        :param content: Conteúdo HTML da página.
        :return: Lista com os links dos PDFs.
        """
        target_names = [name.lower() for name in self.target_names]

        soup = BeautifulSoup(content, "html.parser")
        pdf_links = []

        for link in soup.select("a[href$='.pdf']"):
            text = link.get_text().strip().lower()

            if any(name in text for name in target_names):
                pdf_url = urljoin(self.base_url, link["href"])
                pdf_links.append((text, pdf_url))
                logging.info(f"[Links] Link encontrado: '{text}' -> {pdf_url}")

        if not pdf_links:
            logging.warning(f"[Links] Nenhum link encontrado para os anexos: {', '.join(target_names)}.")
        else:
            logging.info(f"[Links] Total de links encontrados: {len(pdf_links)}.")

        return pdf_links

    def get_page_content(self, url: str, timeout: int = 10) -> bytes:
        """
        Faz o download do conteúdo da página.

        :param url: URL da página a ser baixada.
        :param timeout: Tempo limite para a requisição.
        :return: Conteúdo da página.
        """
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            logging.error(f"[Erro] Falha ao acessar a URL '{url}'. Detalhes: {e}")
            raise

    def run(self) -> None:
        """
        Executa o processo completo de scraping.
        """
        try:
            logging.info(f"[Execução] Iniciando o processo de scraping para a URL base: '{self.base_url}'.")
            content = self.get_page_content(self.base_url)
            pdf_links = self.find_pdf_links(content)

            if not pdf_links:
                logging.info("[Execução] Nenhum PDF correspondente encontrado. Processo encerrado.")
                return

            downloaded_files = []

            for name, pdf_url in pdf_links:
                logging.info(f"[Download] Iniciando download do arquivo '{name}' de '{pdf_url}'.")
                downloaded_files.append(self.download_file(pdf_url))

            if downloaded_files:
                logging.info("[Compressão] Compactando os arquivos baixados em um único arquivo ZIP.")
                self.compress_files(downloaded_files)
                logging.info("[Execução] Processo de scraping concluído com sucesso.")
        except Exception as e:
            logging.error("[Erro] Ocorreu um erro durante o processo de scraping.")
            raise


if __name__ == "__main__":
    base_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    target_names = ["Anexo I", "Anexo II"]

    scraper = ANSScraper(base_url, target_names)
    scraper.run()
