import pandas as pd

data = {
    'Produto' : ["Calça", "Saia", "Blusa", "Camiseta", "Vestido"],
    'Janeiro' : [12, 24, 36, 6, 18],
    'Fevereiro' : [13, 26, 39, 7, 21],
    'Março' : [10, 20, 30, 5, 15]
}

tabela = pd.DataFrame(data)

# Obter índice da linha com o maior valor de quantidade de vendas em janeiro
indice = tabela["Janeiro"].idxmax()
produto = tabela["Produto"][indice]

print(indice)
print(produto)

indice_camiseta = tabela[tabela["Produto"] == "Camiseta"].index.values
print(indice_camiseta)

camisetas_janeiro = tabela["Janeiro"].loc[tabela.index[3]]
camisetas_fevereiro = tabela["Fevereiro"].loc[tabela.index[3]]
print(camisetas_janeiro)
print(camisetas_fevereiro)

aumento_percentual = (camisetas_fevereiro * 100) / camisetas_janeiro
print("Aumento percentual:", aumento_percentual)