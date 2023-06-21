import pathlib
import pandas as pd

tabela = pd.read_csv(pathlib.Path("Analisis de tabela/clientes.csv"), encoding="latin1", sep=';')
tabela = tabela.drop(columns=["Unnamed: 8", "Idade"])
print(tabela)