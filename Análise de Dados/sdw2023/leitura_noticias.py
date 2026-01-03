import pandas as pd
import json


# df_usuarios = pd.read_csv("./usuarios.csv", sep=";")
# df_news = pd.read_csv("./news.csv", sep=";")


def merge_csvs(csv_1, csv_2):
    """Carrega dois arquivos CSV, mescla-os e exibe colunas especificas
    Args:
        csv_1 (str): O caminho para o arquivo csv de usuarios.
        csv_2 (str): O caminho para o csv de notícias.
    """

    try:
        df_usuarios = pd.read_csv("./usuarios.csv", sep=";")
        df_news = pd.read_csv("./news.csv", sep=";")

        # realizar o merge (junção) pela coluna user_id

        df_merged = pd.merge(df_usuarios, df_news, on="user_id", how="inner")

        colunas_desejadas = [
            "nome",
            "email",
            "tipo_conta",
            "agencia",
            "description",
            "icon",
        ]

        for col in colunas_desejadas:
            if col not in df_merged.columns:
                print(
                    f" ❌Erro: A coluna: '{col}' não foi encontrada nos arquivos CSV mesclados."
                )
                print(f"Colunas disponíveis: {list(df_merged.columns)}")
                return

        # Criar o dataframe final com apenas as colunas selecionadas
        df_final_merged = df_merged[colunas_desejadas]

        # Exibiro resultado com uma tabela
        print("Resultado dados enriquecidos após a carga:")
        df_final = df_final_merged.to_dict(orient="records")

        json_output = json.dumps(df_final, indent=4, ensure_ascii=False)

        print(json_output)

    except FileNotFoundError:
        print(f"❌ Um dos arquivos não foi encontrado.")
        print(f"Certifique-se de que '{csv_1}' e '{csv_2}' estão no diretório.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    usuarios_csv = "./usuarios.csv"
    news_csv = "./news.csv"
    merge_csvs(usuarios_csv, news_csv)
