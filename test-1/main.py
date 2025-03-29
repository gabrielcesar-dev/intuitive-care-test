import os
import requests


class ANSScraper:
    def __init__(self, base_url, output_dir="downloads"):
        """
        Inicializa o scraper com a URL base e diretório de saída

        :param base_url: URL base do site a ser raspado
        :param output_dir: Diretório onde os arquivos serão salvos
        """
        self.base_url = base_url
        self.output_dir = output_dir
        self.session = requests.Session()

        # Cria o diretório de saída se não existir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
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
            print("Página acessada com sucesso.")

            
        except Exception as e:
            print(f"Erro durante o processo: {e}")
            return None

if __name__ == "__main__":
    base_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    scraper = ANSScraper(base_url)
    result = scraper.run()
    