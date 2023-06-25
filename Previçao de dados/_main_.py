import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import seaborn as sns

tabela = pd.read_csv("Previçao de dados/barcos_ref.csv")

x, y = tabela.drop(columns="Preco"), tabela["Preco"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

linear_model = LinearRegression().fit(x_train, y_train)
forest_model = RandomForestRegressor().fit(x_train, y_train)
# sns.heatmap(tabela.corr()[["Preco", "Largura"]], annot=True, cmap="Blues")
forest_p = forest_model.predict(x_test)

new_tabel = pd.DataFrame()
new_tabel["Y"] = y_test
new_tabel["Tree"] = forest_p

plt.figure(figsize=(15, 6))
sns.lineplot(data=new_tabel)
plt.show()

new_ships = pd.read_csv("Previçao de dados/novos_barcos.csv")
new_predict= forest_model.predict(new_ships)
print(new_predict)
