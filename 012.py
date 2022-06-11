preco = float(input("Qual é o preço do produto? R$: "))
desconto = int(input("Quantos porcento de desconto? "))

valor = preco - (desconto/100 * preco)
print(f"O produto que custava {preco}, na promoção com desconto de {desconto}% vai sair por {valor}")