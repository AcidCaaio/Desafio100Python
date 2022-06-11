from math import ceil
dias = int(input("Quantos dias o carro ficou alugado?: "))
km = int(input("Quantos kilômetros foram rodados?: "))

pagar = ceil((60*dias) + (0.15 * km))

print(f"O valor total a se pagar é de R$: {pagar}")