Lp = float(input("Qual a largura da sua parede em metros? "))
Ap = float(input("Qual a altura da sua parede em metros? "))
area = Lp * Ap
# Sabendo que cada litro de tinta pinta 2 metros
litros = area / 2

print(f"Sua parede tem as dimensões de {Lp} x {Ap} e sua área total é de: {area:.2f}")
print(f"Para pintar a sua parede, serão necessárias {litros:2f} de tinta")