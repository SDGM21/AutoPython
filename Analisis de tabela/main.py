from get_tabela_data import get_tabela
import plotly.express as px
if __name__ == '__main__':
    # for cols in get_tabela().columns:
        
    grafico = px.histogram(get_tabela(), x=get_tabela().columns[2], y="Nota (1-100)", text_auto=True, histfunc='avg', nbins=10)
        # pass
    grafico.show()
    pass