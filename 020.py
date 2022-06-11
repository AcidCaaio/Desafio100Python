from random import sample

a1 = input("Nome do primeiro aluno: ")
a2 = input("Nome do segundo aluno: ")
a3 = input("Nome do terceiro aluno: ")
a4 = input("Nome do terceiro aluno: ")

lista = [a1, a2, a3, a4]
lista2 = sample(lista, k=len(lista))

print(lista2)
print(f"O aluno escolhido foi: {lista2[0]}")