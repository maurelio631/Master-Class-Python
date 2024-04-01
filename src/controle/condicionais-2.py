print("Informe seu ano de nascimento: ")
ano = int(input("Em que ano você nasceu? "))

if ano>=1946 and ano<=1964:
        print("Geração Baby Boomer")
elif ano>=1965 and ano <=1980: #Else If
        print("Geração X")
elif ano>=1981 and ano <=1996:
        print("Geração Y")
elif ano>=1997 and ano<=2010:
        print("Geração Z")
else: print("Geração Alfa")
    
