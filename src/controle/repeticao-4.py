produto = {
    "nome":"Notebook",
    "preco":4859.45,
    "quantidade":42,
}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave,valor in produto.items():
    print(f"{chave}=>{valor}")

for chave in produto:
    print(f"{chave}=>{produto[chave]}")