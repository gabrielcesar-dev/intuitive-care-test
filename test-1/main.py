import os
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import zipfile


class ANSScraper:
    def __init__(self, base_url, target_names=None, output_dir="downloads"):
        """
        Inicializa o scraper com a URL base e diretório de saída

        :param base_url: URL base do site a ser raspado
        :param output_dir: Diretório onde os arquivos serão salvos
        """
        self.base_url = base_url
        self.target_names = target_names
        self.output_dir = output_dir
        self.session = requests.Session()

        # Cria o diretório de saída se não existir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def compress_files(self, filepaths, output_filename="anexos.zip"):
        """
        Compacta os arquivos baixados em um único arquivo ZIP

        :param filepaths: Lista de caminhos dos arquivos a serem compactados
        :param output_filename: Nome do arquivo ZIP de saída
        :return: Caminho do arquivo ZIP gerado
        """
        output_path = os.path.join(self.output_dir, output_filename)
        
        if os.path.exists(output_path):
            print(f"Atenção: O arquivo {output_path} já existe e será sobrescrito.")
        
        print(f"Compactando {len(filepaths)} arquivos em {output_path}")
        
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for filepath in filepaths:
                zipf.write(filepath, os.path.basename(filepath))
                print(f"Arquivo {filepath} adicionado ao ZIP")
        
        print(f"Compactação concluída: {output_path}")

        return output_path

    def download_file(self, url):
        """
        Faz o download de um arquivo e o salva no diretório especificado

        :param url: URL do arquivo a ser baixado
        :return: Caminho do arquivo salvo
        """
        filename = os.path.basename(url)
        file_path = os.path.join(self.output_dir, filename)

        # Verifica se o arquivo já existe
        if os.path.exists(file_path):
            print(f"Arquivo {filename} já existe. Pulando download.")
            return file_path

        content = self.get_page_content(url)

        with open(file_path, 'wb') as file:
            file.write(content)

        print(f"Arquivo {filename} baixado com sucesso.")

        return file_path


    def find_pdf_links(self, content):
        """
        Encontra os links dos Anexos I e II na página a partir do conteúdo HTML.
        :param content: Conteúdo HTML da página
        :return: Lista com os links dos PDFs
        """
        target_names = [name.lower() for name in self.target_names]

        soup = BeautifulSoup(content, 'html.parser')
        pdf_links = []

        for link in soup.select("a[href$='.pdf']"):
            text = link.get_text().strip().lower()

            if any(name in text for name in target_names):
                pdf_url = urljoin(self.base_url, link['href'])
                pdf_links.append((text, pdf_url))
                
                print(f"Encontrado link: {text} -> {pdf_url}")
            
        if not pdf_links:
            print("Nenhum link encontrado para os anexos: " + ", ".join(target_names))
            return []

        return pdf_links

    
    def get_page_content(self, url, timeout=10):
        """
        Faz o download do conteúdo da página

        :param url: URL da página a ser baixada
        :param timeout: Tempo limite para a requisição
        :return: Conteúdo da página
        """
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()

            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
            raise
    
    def run(self):
        """
        Executa o processo completo de scraping
        """
        try:
            content = self.get_page_content(self.base_url)
            pdf_links = self.find_pdf_links(content)

            if not pdf_links:
                print("Nenhum PDF correspondente encontrado. Processo encerrado.")
                return

            downloaded_files = []

            for name, pdf_url in pdf_links:
                print(f"Baixando {name} de {pdf_url}")
                downloaded_files.append(self.download_file(pdf_url))

            if downloaded_files:
                print("Compactando arquivos baixados...")
                self.compress_files(downloaded_files)
                print("Processo concluído com sucesso.")
        except Exception as e:
            print(f"Erro durante o processo: {e}")
            raise

if __name__ == "__main__":
    base_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    target_names = ["Anexo I", "Anexo II"]
    
    scraper = ANSScraper(base_url, target_names)
    result = scraper.run()
