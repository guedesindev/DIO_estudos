import os
import pandas as pd
from extract import extract_data
from messages import obter_noticia_dinamica
from tqdm import tqdm

file_path = "./news.csv"
colunas = ["id", "user_id", "icon", "description"]


def transform_data(usuarios_df, ids_df):
    user_ids = ids_df["UserId"].astype(int).tolist()
    usuarios_filtrados = usuarios_df[usuarios_df["id_usuario"].isin(user_ids)].copy()

    usuarios_filtrados["news_description"] = usuarios_filtrados.apply(
        obter_noticia_dinamica, axis=1
    )
    usuarios_filtrados["news_icon"] = (
        "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg"
    )

    return usuarios_filtrados[["id_usuario", "nome", "news_description", "news_icon"]]
