# nome = str(input("Qual é o seu nome ? "))
# if nome.lower() == 'gustavo':
#     print("Gustavo é um nome muito bonito!")
# elif nome.lower()  == 'pedro' or nome.lower()  == 'maria' or nome.lower()  == 'paulo':
#     print(" O seu nome é bem popular no Brasil")
# elif nome.lower()  in ('ana','claudia','jéssica','juliana'):
#     print ("Que belo nome feminino")
# else:
#     print("Seu nome é bem normal")
# print(f"Bom dia {nome}! ")
from math import ceil

valor =  float(input("Qual o valor da casa? "))
renda = float(input("Qual o salário mensal? "))
anos = int(input("Quantos anos vai realizar o pagamento? "))

meses = (anos*12)

percentagem = renda*0.3

parcela = valor / meses

if parcela >= percentagem:
    print(f"A parcela comprometará mais de 30% do salário do comprador com o valor de R$:{ceil(parcela)} devido a isso a compra está rejeitada!")
else:
    print(f"Compra aprovada!, a parcela mensal será de R$: {parcela:.2f}")