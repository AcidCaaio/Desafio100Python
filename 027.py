n = str(input("Qual é o seu nome completo ?: ")).strip()
nome = n.split()
print(nome)
print("Prazer em te conhecer! meu criador se chama Caio")
print(f"{(nome[0])} é o seu primeiro nome e {(nome[-1])} é o seu ultimo nome")
