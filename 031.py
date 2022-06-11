d = float(input("Qual a distância da sua viagem em kilômetros?"))

if d <= 200:
   valor = d * 0.5
   print(f"O valor da viagem é R$: {valor}")
else:
    valor = d * 0.45
    print(f"O valor da viagem é R$: {valor}")
