from get_tabela_data import get_tabela
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.subplot(131)
    plt.bar(
        x=get_tabela()["Salário Anual (R$)"],
        height=get_tabela()["Nota (1-100)"],
        width=100,
    )
    plt.subplot(132)
    plt.bar(
        x=get_tabela()["Experiência Trabalho"].sort_values(),
        height=get_tabela()["Nota (1-100)"].sort_values(),
    )
    plt.show()

    data = dict()
    promedio = float()

    for x in range(100):
        key = get_tabela()["Profissão"].values[x]
        value = get_tabela()["Nota (1-100)"].values[x]
        data.setdefault(key, []).append(value)
        pass

    for key in list(data.keys()):
        notes = data[key]
        for aux in notes:
            promedio = promedio + aux
            pass
        promedio = promedio / len(notes)
        data[key] = promedio
        pass

    plt.bar(x=list(data.keys()), height=list(data.values()))
    plt.show()
pass
