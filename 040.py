n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digiete a segunda nota: "))

media = (n1 + n2)/2

print(f"Tirando {n1} e {n2} sua média é {media}")

if media < 5.0:
    print(f"Sua média foi de abaixo de 5.0")
    print("Você está reprovado!!")

elif 5.0 <= media < 6.9:
    print(f"Sua média não foi boa o suficiente para ser aprovado porém ", end="")
    print("ainda dá para recuperar.\nVocê está de recuperação!!")

else:
    print(f"Sua média foi de maior que 7.0")
    print("Parabéns! Você foi aprovado!")
