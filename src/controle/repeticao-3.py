pergunta = "Deseja continuar? (S/n)"
resposta = input(pergunta)
quantidade = 1

while resposta.lower() != "n":
    print(f"Vamos continuar pela {quantidade} vez")
    resposta = input(pergunta)
    quantidade += 1

print("Fim do exemplo")