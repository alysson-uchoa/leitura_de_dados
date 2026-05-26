import pandas as pd
import time

inicio = time.time()

contador = 0

df = pd.read_csv("base.csv")

base_vendedor = pd.read_csv("base.csv")[["Vendedor"]].drop_duplicates()

for _, linha in base_vendedor.iterrows():
    vendedor = linha["Vendedor"]
    
    valor = df[df["Vendedor"] == vendedor]["Valor da Venda"].sum()
    quantidade = df[df["Vendedor"] == vendedor]["Quantidade"].sum()

    contador += 1

    print(f"{contador} | Vendedor = {vendedor} | Valor = {valor:.2f} | Quantidade = {quantidade}")

fim = time.time()

print(f"\n Tempo total: {fim - inicio:.2f} segundos")