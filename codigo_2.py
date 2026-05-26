import pandas as pd
import time

inicio = time.time()

contador = 0

df = pd.read_csv("base.csv")

base_valor = df.groupby("Vendedor")["Valor da Venda"].sum().to_dict()
base_quantidade = df.groupby("Vendedor")["Quantidade"].sum().to_dict()

base_vendedor = pd.read_csv("base.csv")[["Vendedor"]].drop_duplicates()

for linha in base_vendedor.itertuples(index=False):
    id = linha.Vendedor
    valor = base_valor.get(id, 0)
    quantidade = base_quantidade.get(id, 0)

    contador += 1

    print(f"{contador} | Vendedor = {id} | Valor = {valor} | Quantidade = {quantidade}")

fim = time.time()

print(f"\n Tempo total: {fim - inicio:.2f} segundos")