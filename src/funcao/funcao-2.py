def calcular_media_simples(n1, n2, n3):
    return (n1+n2+n3)/3


def calcular_media_ponderada(n1, n2, n3):
    return (n1*5+n2*3+n3*2)/10

def melhor_media(n1,n2,n3):
    m1 = calcular_media_simples(n1,n2,n3)
    m2 = calcular_media_ponderada(n1,n2,n3)

    return m1 if m1>m2 else m2

resultado1 =  melhor_media(5,6,9)
resultado2 =  melhor_media(9,6,5)

print(resultado1)
print(resultado2)