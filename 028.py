# num = int(input("Vou te dar duas chances de acertar o número que eu pensei. De 0 a 5 qual o número você escolhe?: "))
# while num !=0:
#     print(input("Tente novamente:"))
#     print("Processando...")
#     if num == 0:
#         print("Processandoo...")
#         print("Parabéns! Você certou!")
#     else:
#         print("Ganhei! Você não acertou o número que eu pensei!")
#
from random import randint
from time import sleep

computador = randint(0, 5)  # Faz o computador pensar no número
pessoa = int(input("Vou te dar duas chances de acertar o número que eu pensei. De 0 a 5 qual o número você escolhe?: "))
if pessoa == computador:
    print("Processando...")
    sleep(1)
    print(f"Você acertou! Eu pensei no número {computador} e você também!")
else:
    print("Processando...")
    sleep(2)
    print(f"Infelizmente você perdeu. Eu pensei no número {computador} e você no número {pessoa}")
