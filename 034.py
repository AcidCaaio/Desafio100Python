salario = float(input("Qual é o salário do funcionário? R$:"))

salario1 = salario * 1.10 if salario > 1250 else salario * 1.15

print(f"O funcionário que recebia {salario}, passa a receber {salario1}")

# if salario > 1250:
#     salario1 = (salario * 0.10 ) + salario
#     print(f"O funcionário que recebia {salario}, passa a receber {salario1}")
# if salario < 1250:
#     salario1 = (salario * 0.15) + salario
#     print(f"O funcionário que recebia {salario}, passa a receber {salario1}")