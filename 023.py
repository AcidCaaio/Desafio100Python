num = int(input('Digite um numero inteiro positivo: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f"{unidade} , {dezena}, {centena}, {milhar}")