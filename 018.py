from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo que você deseja: "))

seno = sin (radians(angulo))
coseno = cos (radians(angulo))
tangente = tan (radians(angulo))

print(f"O seno de {angulo} é {seno:.2f}:")
print(f"O cosseno de {angulo} é {coseno:.2f}")
print(f"A tangente de {angulo} é {tangente:.2f}")
