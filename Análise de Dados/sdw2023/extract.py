import pandas as pd


def extract_data():
    usuarios = pd.read_csv("./usuarios.csv", sep=";")
    ids = pd.read_csv("./ids.csv")

    return usuarios, ids
