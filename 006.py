import math
C = int(input("Digite um valor: "))
# dobro = n * 2
# triplo = n * 3
raiz_quadrada = math.sqrt(C)

print(f"O valor digitado foi: {C} \nO do dobro de {C} é: {C*2} \nO triplo de {C} é: {C*3}")
print("A raiz quadrada de {} é: {:.2f}." .format(C, raiz_quadrada))