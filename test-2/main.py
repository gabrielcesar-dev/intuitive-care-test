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

        logging.info(f"Output directory set to: {output_dir}")

    def save_to_csv(self, df: pd.DataFrame) -> str:
        """
        Salva o DataFrame em um arquivo CSV.
        :param df: DataFrame a ser salvo.
        :return: Caminho do arquivo CSV salvo.
        """
        try:
            csv_path = os.path.join(self.output_dir, f"{self.output_filename}.csv")
            df.to_csv(csv_path, index=False, encoding='utf-8')
            logging.info(f"CSV file successfully saved at: {csv_path}")
            return csv_path
        except Exception as e:
            logging.error(f"Failed to save CSV file. Error: {e}")
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
            logging.info(f"File successfully compressed into ZIP at: {zip_path}")
            return zip_path
        except Exception as e:
            logging.error(f"Failed to compress file into ZIP. Error: {e}")
            raise

    def extract_tables_from_pdf(self) -> pd.DataFrame:
        """
        Extrai todas as tabelas de todas as páginas do PDF e as concatena em um único DataFrame.
        Substitui as abreviações das colunas OD e AMB pelas descrições completas.
        :return: DataFrame contendo todas as tabelas extraídas.
        """
        try:
            logging.info(f"Starting table extraction from PDF: {self.input_pdf_path}")
            all_tables = []

            with pdfplumber.open(self.input_pdf_path) as pdf:
                for page_number, page in enumerate(pdf.pages, start=1):
                    table = page.extract_table()

                    if table:
                        df = pd.DataFrame(table[1:], columns=table[0])
                        
                        # Substituir as abreviações pelas descrições completas
                        df.rename(columns={
                            "OD": "Seg. Odontológica",
                            "AMB": "Seg. Ambulatorial"
                        }, inplace=True)
                        
                        all_tables.append(df)
                        logging.info(f"Table successfully extracted from page {page_number}")
                    else:
                        logging.warning(f"No table found on page {page_number}")

            if all_tables:
                combined_df = pd.concat(all_tables, ignore_index=True)
                logging.info("All tables successfully extracted and combined into a single DataFrame.")
                return combined_df
            else:
                logging.warning("No tables were found in the entire PDF.")
                return pd.DataFrame()

        except Exception as e:
            logging.error(f"Error occurred while extracting tables from PDF. Error: {e}")
            raise

    def run(self) -> str:
        """
        Executa o processo completo de extração, transformação e carga dos dados.
        :return: Caminho do arquivo ZIP criado.
        """
        try:
            logging.info("Process started: Extracting, transforming, and compressing data.")
            df = self.extract_tables_from_pdf()
            if df.empty:
                raise ValueError("No tables were extracted from the PDF.")
            
            csv_path = self.save_to_csv(df)

            zip_path = self.compress_to_zip(csv_path)

            logging.info(f"Process completed successfully. ZIP file available at: {zip_path}")
            return zip_path

        except Exception as e:
            logging.error(f"Process failed. Error: {e}")
            raise

if __name__ == "__main__":
    input_pdf = "Anexo_I.pdf"
    output_filename = "Teste_GabrielCesarSilvinoXavier"

    transformer = ANSDataTransformer(input_pdf_path=input_pdf, output_dir="output", output_filename=output_filename)
    transformer.run()