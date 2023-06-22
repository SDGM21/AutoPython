import pathlib
from kiwisolver import UnknownConstraint
import pandas as pd


def get_tabela():
    tabela = pd.read_csv(
        pathlib.Path("Analisis de tabela/clientes.csv"), encoding="latin1", sep=";"  # type: ignore
    )
    tabela = tabela.drop(columns=["Unnamed: 8"])
    tabela = tabela.dropna()
    tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], "coerce")
    return tabela
