vel = float(input("Qual a velocidade atual do carro? "))

if vel <= 80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print("Multado! \nVocê excedeu o limite máximo da via que é de 80km/h!")
    print(f"Você deve pagar uma multa de R${((vel-80)*7):.2f}")
    print("Tenha um bom dia")