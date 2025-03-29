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

    def find_pdf_links(self, content):
        """
        Encontra os links dos Anexos I e II na página a partir do conteúdo HTML.
        :param content: Conteúdo HTML da página
        :return: Dicionário com os links dos PDFs
        """
        target_names = [name.lower() for name in self.target_names]

        soup = BeautifulSoup(content, 'html.parser')
        pdf_links = {}

        for link in soup.select("a[href$='.pdf']"):
            text = link.get_text().strip().lower()

            # Verifica se o texto do link contém algum dos nomes-alvo
            for name in target_names:
                if name in text:
                    pdf_url = urljoin(self.base_url, link['href'])
                    pdf_links[name] = pdf_url
                    print(f"Encontrado: {name} -> {pdf_url}")

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

            
        except Exception as e:
            print(f"Erro durante o processo: {e}")
            return None

if __name__ == "__main__":
    base_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    target_names = ["anexo i", "anexo ii"]
    
    scraper = ANSScraper(base_url, target_names)
    result = scraper.run()
    