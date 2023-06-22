from get_tabela_data import get_tabela
import plotly.express as px
import matplotlib.pyplot as plt
if __name__ == '__main__':

    salarios = get_tabela()[get_tabela().columns[3]]
    edades = get_tabela()[get_tabela().columns[2]]
        
    plt.bar(x=salarios, 
            height=edades,
            width=get_tabela().__len__())
    
    plt.xlabel("Salario")
    plt.ylabel("Edad")
    plt.show()


pass    
  