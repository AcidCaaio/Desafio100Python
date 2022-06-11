frase = str(input("Insira a frase a ser analizada:")).strip().upper()
print(f"A quantidade de letras 'A' no texto é dê: {frase.count('A')}")
print(f"A primeira letra 'A' aparece na posição:{frase.find('A')+1}")
print(f"A ultima apariçãod a letra 'A' é na posição: {frase.rfind('A')+1}")