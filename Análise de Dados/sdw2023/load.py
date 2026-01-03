import pandas as pd
import os


def load_data(df_transformado, file_path="news.csv"):
    if df_transformado.empty:
        print("⚠️ Sem dados para carregar.")
        return

    if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
        df_existente = pd.read_csv(file_path, sep=";", usecols=["id"])
        ultimo_id = df_existente["id"].max()
    else:
        ultimo_id = 0

    proximo_id = ultimo_id + 1

    news_to_save = df_transformado.rename(
        columns={
            "id_usuario": "user_id",
            "news_description": "description",
            "news_icon": "icon",
        }
    )

    news_to_save["id"] = range(proximo_id, proximo_id + len(news_to_save))

    news_to_save = news_to_save[["id", "user_id", "icon", "description"]]

    header_needed = not os.path.exists(file_path) or os.stat(file_path).st_size == 0

    try:
        news_to_save.to_csv(
            file_path,
            mode="a",
            sep=";",
            index=False,
            header=header_needed,
            encoding="utf-8",
        )
    except Exception as e:
        print("❌ Erro ao gravar no ficheiro: {e}")
        raise e
