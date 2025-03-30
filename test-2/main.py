import os
import zipfile
import pandas as pd
import pdfplumber
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data-transform.log"),
        logging.StreamHandler()
    ]
)

class ANSDataTransformer:
    def __init__(self, input_pdf_path: str, output_dir: str = "output", output_filename: str = "candidato"):
        """
        Inicializa a classe com o caminho do PDF de entrada, diretório de saída e nome do arquivo de saída.

        :param input_pdf_path: Caminho do arquivo PDF de entrada.
        :param output_dir: Diretório onde os arquivos de saída serão salvos.
        :param output_filename: Nome base para os arquivos de saída.
        """
        self.input_pdf_path = input_pdf_path
        self.output_dir = output_dir
        self.output_filename = output_filename

        # Garante que o diretório de saída existe
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        logging.info(f"[Configuração] Diretório de saída definido para: {output_dir}")

    def save_to_csv(self, df: pd.DataFrame) -> str:
        """
        Salva o DataFrame em um arquivo CSV.
        :param df: DataFrame a ser salvo.
        :return: Caminho do arquivo CSV salvo.
        """
        try:
            csv_path = os.path.join(self.output_dir, f"{self.output_filename}.csv")
            df.to_csv(csv_path, index=False, encoding='utf-8')
            logging.info(f"[CSV] Arquivo CSV salvo com sucesso em: {csv_path}")
            return csv_path
        except Exception as e:
            logging.error(f"[CSV] Falha ao salvar o arquivo CSV. Detalhes: {e}")
            raise

    def compress_to_zip(self, file_path: str) -> str:
        """
        Compacta o arquivo especificado em um arquivo ZIP.
        :param file_path: Caminho do arquivo a ser compactado.
        :return: Caminho do arquivo ZIP criado.
        """
        try:
            zip_path = os.path.join(self.output_dir, f"{self.output_filename}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(file_path, os.path.basename(file_path))
            logging.info(f"[Compressão] Arquivo compactado com sucesso em: {zip_path}")
            return zip_path
        except Exception as e:
            logging.error(f"[Compressão] Falha ao compactar o arquivo. Detalhes: {e}")
            raise

    def extract_tables_from_pdf(self) -> pd.DataFrame:
        """
        Extrai todas as tabelas de todas as páginas do PDF e as concatena em um único DataFrame.
        :return: DataFrame contendo todas as tabelas extraídas.
        """
        try:
            logging.info(f"[Extração] Iniciando extração de tabelas do PDF: {self.input_pdf_path}")
            all_tables = []

            with pdfplumber.open(self.input_pdf_path) as pdf:
                for page_number, page in enumerate(pdf.pages, start=1):
                    table = page.extract_table()

                    if table:
                        df = pd.DataFrame(table[1:], columns=table[0])
                        all_tables.append(df)
                        logging.info(f"[Extração] Tabela extraída com sucesso da página {page_number}")
                    else:
                        logging.warning(f"[Extração] Nenhuma tabela encontrada na página {page_number}")

            if all_tables:
                combined_df = pd.concat(all_tables, ignore_index=True)
                logging.info("[Extração] Todas as tabelas foram extraídas e combinadas em um único DataFrame.")
                return combined_df
            else:
                logging.warning("[Extração] Nenhuma tabela foi encontrada no PDF.")
                return pd.DataFrame()

        except Exception as e:
            logging.error(f"[Extração] Erro ao extrair tabelas do PDF. Detalhes: {e}")
            raise

    def run(self) -> str:
        """
        Executa o processo completo de extração, transformação e carga dos dados.
        :return: Caminho do arquivo ZIP criado.
        """
        try:
            logging.info("[Execução] Processo iniciado: Extração, transformação e compactação de dados.")
            df = self.extract_tables_from_pdf()
            if df.empty:
                raise ValueError("No tables were extracted from the PDF.")
            
            csv_path = self.save_to_csv(df)

            zip_path = self.compress_to_zip(csv_path)

            logging.info(f"[Execução] Processo concluído com sucesso. Arquivo ZIP disponível em: {zip_path}")
            return zip_path

        except Exception as e:
            logging.error(f"[Execução] Processo falhou. Detalhes: {e}")
            raise

if __name__ == "__main__":
    input_pdf = "Anexo_I.pdf"
    output_filename = "Teste_GabrielCesarSilvinoXavier"

    transformer = ANSDataTransformer(input_pdf_path=input_pdf, output_dir="output", output_filename=output_filename)
    transformer.run()
