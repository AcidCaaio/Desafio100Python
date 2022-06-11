from math import sqrt , pow, hypot
cateto_oposto = float(input("Qual o valor do cateto oposto do triangulo: "))
cateto_adjacente = float(input("Qual o valor do cateto adjacente do triangulo: "))
# hipotenusa = math.sqrt((math.pow(cateto_adjacente, 2) + pow(cateto_oposto, 2)))
# sem importação
#  hi = (co ** 2 + ca ** 2) ** (1/2)
#Hipotenusa pode ser calculada direto usando a função (HYPOT)
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"O valor da hipotenuse é : {hipotenusa:.2f}")