from pathlib import Path
from selenium import webdriver
import pandas as pd

nav = webdriver.Chrome()

tabela = pd.read_excel(Path("Generaçao de tabelas/commodities.xlsx"))

for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"].__str__()
    produto = (
        produto.replace("ó", "o")
        .replace("ã", "a")
        .replace("á", "a")
        .replace("ç", "c")
        .replace("ú", "u")
        .replace("é", "e")
    )

    link = f"https://www.melhorcambio.com/{produto}-hoje"
    nav.get(link)

    preco = (
        str(nav.find_element("xpath", '//*[@id="comercial"]').get_attribute("value"))
        if nav.find_element("xpath", '//*[@id="comercial"]').get_attribute("value")
        != None
        else False
    )
    preco = preco.replace(".", "").replace(",", ".") if preco else 0
    tabela.loc[linha, "Preço Atual"] = float(preco)
    pass

nav.quit()
tabela["Comprar"] = tabela["Preço Ideal"] > tabela["Preço Atual"]
tabela.to_excel("Generaçao de tabelas/commodities_atual.xlsx", index=False)
