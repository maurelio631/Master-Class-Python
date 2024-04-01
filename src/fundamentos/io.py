print("Informe seu nome: ")
nome = input() #Receber a entrada do usuário

print("Informe sua idade: ")
idade = int(input())#Casting

#F-String
#String interpolada
print(f"Olá, {nome}! Você tem {idade+2} anos.") #Vai gerar um problema, pois a entrada do usuário sempre será string
print(f"Olá, {nome}! Você tem {idade} anos.")