
import os
os.system('cls')
n1 = int(2022)
n2 = int(input("Sua idade:\n"))
resposta = input("Já fez aniversário esse ano? \ns = sim \nn = não\n")
if resposta == "s":
    n3 = 1
else:
    n3 = 2
if n3 == 1:
    n4 = n1 - n2
else:
    n4 = n1 - n2 + 1
print (n4)