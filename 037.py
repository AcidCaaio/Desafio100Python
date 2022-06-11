numero = int(input("Digite o número que quer converter: "))
print(f"O número que você quer converter é: {numero} \nEscolha para qual base numérica.")
x = int(input('''
[1] - para Binário 
[2] - para Octadecimal
[3] - para Hexadecimal
[4] - para todas as outras opções
[0] - para finalizar o programa
A opção escolhida é: '''))

if x == 1:
    binario = format(numero, "b")
    print(f"O valor {numero} convertido em binário é igual a: {binario}")

elif x == 2:
    octa = format(numero, "o")
    print(f"O valor {numero} convertido em octadecimal é igual a: {octa}")

elif x == 3:
    hexa = format(numero, "x")
    print(f"O valor {numero} convertido em hexadecimal é igual a: {hexa}")

elif x == 4:
    hexa = format(numero, "x")
    octa = format(numero, "o")
    binario = format(numero, "b")
    print("Você escolheu em todas as bases")
    print(f"O valor {numero} convertido em binário é igual a: {binario}")
    print(f"O valor {numero} convertido em octadecimal é igual a: {octa}")
    print(f"O valor {numero} convertido em hexadecimal é igual a: {hexa}")

elif x == 0:
    print("Você optou em terminar o programa. Tchau Tchau!")

else:
    print('''Opção inválida!!
    Terminando o programa''')
