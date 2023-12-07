import pandas as pd
data = {
    'Nome': ["Lara", "Helena", "Kelly", "Mila"],
    'Idade': [20, 15, 23, 36],
    'Cidade': ["Brasília", "Cabo Frio", "Xique Xique", "Barrocas"]
}

tabela = pd.DataFrame(data)
print(tabela)

for dado in tabela.values:
    #print(dado)
    print(dado[0], dado[1])