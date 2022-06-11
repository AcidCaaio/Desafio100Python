# a, b = map(int, input("Qual o valor de a e B: ").split())
# soma = 0
# for x in range(1, a+1):
#     for y in range(1, b+1):
#         soma += (y-1) + (x+1)
# print(soma)

# janeiro = int(input("Vendas no mês de janeiro: "))
# fevereiro = int(input("Vendas no mês de fevereiro: "))
# marco = int(input("Vendas no mês de março: "))
# abril = int(input("Vendas no mês de abril: "))
#
# media = (janeiro+fevereiro+abril+marco)/4
# soma = janeiro+fevereiro+abril+marco
# if media <= 60:
#     print(f"O volume de vendas do funcionário no primeiro quadrimestre foi dê {soma}"
#       f", alcançando a méta de {media} vendas por mês")
# else:
#     print(f"O volume de vendas do funcionário no primeiro quadrimestre foi dê {soma}"
#      f", obtendo uma média de {media} abaixo do valor especificado para este mês")

#
n = int(input("tabuada do número?: "))
numero = 1
tabuada = 0
while tabuada != 10:
    tabuada +=1
    valor = n * tabuada
    print(f"9 x {tabuada} = {valor}")
print("x"*10,"Final do programa","x"*10)
