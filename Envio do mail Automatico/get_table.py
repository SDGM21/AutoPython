import pandas as pd

def exec_Table(table_dir):
    table = pd.read_csv(table_dir, sep=";")
    
    total_gasto:float = table["ValorFinal"].sum()
    quantidade:float = table["Quantidade"].sum()
    media:float = total_gasto / quantidade

    return [total_gasto, quantidade, media]

    