import os
import pandas as pd
import pdfplumber


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

        print(f"Diretório de saída definido: {output_dir}")

    def extract_tables_from_pdf(self) -> pd.DataFrame:
        """
        Extrai todas as tabelas de todas as páginas do PDF e as concatena em um único DataFrame.
        :return: DataFrame contendo todas as tabelas extraídas.
        """
        try:
            print(f"Extraindo tabelas do PDF: {self.input_pdf_path}")
            all_tables = []

            with pdfplumber.open(self.input_pdf_path) as pdf:
                for page_number, page in enumerate(pdf.pages, start=1):
                    table = page.extract_table()

                    if table:
                        df = pd.DataFrame(table[1:], columns=table[0])
                        all_tables.append(df)
                        print(f"Tabela extraída da página {page_number}")
                    else:
                        print(f"Nenhuma tabela encontrada na página {page_number}")

            if all_tables:
                combined_df = pd.concat(all_tables, ignore_index=True)
                print("Todas as tabelas foram extraídas e combinadas com sucesso.")
                return combined_df
            else:
                print("Nenhuma tabela foi encontrada no PDF.")
                return pd.DataFrame()

        except Exception as e:
            print(f"Erro ao extrair tabelas do PDF")
            raise

    def run(self) -> str:
        """
        Executa o processo completo de extração, transformação e carga dos dados.
        :return: Caminho do arquivo ZIP criado.
        """
        try:
            df = self.extract_tables_from_pdf()
            if df.empty:
                raise ValueError("Nenhuma tabela foi extraída do PDF.")

        except Exception as e:
            print(f"Erro durante o processo")
            raise

if __name__ == "__main__":
    input_pdf = "Anexo_I.pdf"
    output_filename = "Teste_GabrielCesarSilvinoXavier"

    transformer = ANSDataTransformer(input_pdf_path=input_pdf, output_dir="output", output_filename=output_filename)
    transformer.run()
