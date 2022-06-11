from calendar import isleap
from datetime import date
# ano = int(input("Qual ano deseja analizar? \n Atenção: 0 significa este ano: "))
# while ano == 0:
#     if calendar.isleap(2022) == True:
#         print(f"o ano de 2022 é bissexto")
#     else:
#         print(f"O ano de 2022 não é bissexto")
#     break
#
# while ano != 0:
#  ano6 = calendar.isleap(ano)
#     if ano6 == True:
#         print("O ano é bissexto")
#     else:
#         print("O ano não é bissexto")
#     break

#
# versão matemática
#
# ano = int(input("Qual ano deseja analizar? \n Atenção: 0 significa este ano: "))
#
# b1 = ano % 100
# b2 = ano % 4
# b3 = ano % 400
# b4 = b1 + b2 + b3
#
# if b4 ==0:
#     print(f"O ano de {ano} é bissexto")
# else:
#     print(f"O ano de {ano} não é bissexto")

# versão mais rebuscada


ano = int(input("Qual ano deseja analizar? \n Atenção: 0 significa este ano: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")