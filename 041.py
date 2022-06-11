from datetime import date

nascimento = int(input("Qual o ano de nascimento do atleta: "))

data = date.today().year
idade = data - nascimento

if idade <=9:
    print(f"O atleta tem: {idade}")
    print(f"Classificação: MIRIM")
elif idade <=14:
    print(f"O atleta tem: {idade}")
    print(f"Classificação: INFANTIL")
elif idade <=19:
    print(f"O atleta tem: {idade}")
    print(f"Classificação: JÚNIOR")
elif idade <= 25:
    print(f"O atleta tem: {idade}")
    print(f"Classificação: SÊNIOR")
else:
    print(f"O atleta tem: {idade}")
    print(f"Classificação: Master")
