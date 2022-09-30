# Jogo de azar que conta as tentativas até acertar o número aleatório de 0 a 10
from random import random

import random
numero_sorteado = random.randrange(0,10)
numero_escolhido = int(input("Escolha um número de 0 a 9 \n"))
numero_invalido = 0
tentativa = 1

while numero_sorteado != numero_escolhido:
    if numero_escolhido not in range(0,10):
        print("Número inválido")
        numero_escolhido = int(input("Escolha um número de 0 a 9 \n"))
        numero_invalido += 1
    else:
        tentativa += 1
        print("Errou, tente de novo")
        numero_escolhido = int(input("Escolha um número de 0 a 9 \n"))

if numero_invalido == 0:
    print("Parabéns, você acertou na ", tentativa, "ª tentativa", sep="")
else:
    print("Parabéns, você acertou depois de ", tentativa + numero_invalido, " tentativas, sendo ", tentativa, " números errados e ", numero_invalido, " números inválidos.", sep="")