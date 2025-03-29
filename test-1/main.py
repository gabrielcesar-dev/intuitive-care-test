import os
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


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

    def download_file(self, url):
        """
        Faz o download de um arquivo e o salva no diretório especificado

        :param url: URL do arquivo a ser baixado
        :param filename: Nome do arquivo para salvar
        """

        content = self.get_page_content(url)
        filename = os.path.basename(url)
        file_path = os.path.join(self.output_dir, filename)

        # Verifica se o arquivo já existe
        if os.path.exists(file_path):
            print(f"Arquivo {filename} já existe. Pulando download.")
            return

        with open(file_path, 'wb') as file:
            file.write(content)

        print(f"Arquivo {filename} baixado com sucesso.")


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
            return None

        return pdf_links

    
    def get_page_content(self, url):
        """
        Faz o download do conteúdo da página

        :param url: URL da página a ser baixada
        :param retry_count: Contador de tentativas
        :return: Conteúdo da página
        """
        try:
            response = self.session.get(url, timeout=10)
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

            
            for name, pdf_url in pdf_links:
                print(f"Baixando {name} de {pdf_url}")
                self.download_file(pdf_url)

            
        except Exception as e:
            print(f"Erro durante o processo: {e}")
            return None

if __name__ == "__main__":
    base_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    target_names = ["Anexo I", "Anexo II"]
    
    scraper = ANSScraper(base_url, target_names)
    result = scraper.run()
    