from datetime import date
nascimento = int(input("Digite o ano do seu nascimento: "))
genero = str(input("Qual seu gênero: ")).strip()

while genero.lower() not in ("masculino", "feminino","homem","mulher","femenino"):
    print("Gênero inválido, por favor tente novamente!")
    genero = str(input("Qual seu gênero: ")).strip()

data = date.today()
ano = data.strftime("%Y")
idade = ano-nascimento

if idade > 18 and genero.lower() in "masculino, homem":
    print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano}.")
    print(f"Você já deveria ter se alistado há {idade - 18} anos atrás.")
    print(f"Seu alistamento foi em {nascimento + 18}.")

elif idade < 18 and genero.lower() in "masculino, homem":
    print(f"Quem nasceu em {nascimento} tem {idade} em {ano}.")
    print(f"Ainda faltam {18 - idade} anos para você se alistar.")
    print(f"Seu alistamento será em: {nascimento + 18}.")

elif idade == 18 and genero.lower() in "masculino, homem":
    print(f"Quem nasceu em {nascimento} tem {idade} anos!")
    print("Você deve se alistar IMEDIATAMENTE!")

elif genero.lower() in "feminino, mulher, femenino":
    print(f"Por ser do gênero feminino, não precisa se alistar.")
