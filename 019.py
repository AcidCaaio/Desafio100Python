from random import choice
a1 = input("Nome do primeiro aluno: ")
a2 = input("Nome do segundo aluno: ")
a3 = input("Nome do terceiro aluno: ")
a4 = input("Nome do terceiro aluno: ")

lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print(f"O aluno sorteado foi {sorteio}")
