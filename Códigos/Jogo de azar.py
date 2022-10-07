# Jogo de azar que conta as tentativas até acertar o número aleatório de 0 a 10
from random import random

import random
# Sorteia um número aleatório entre 0 e 9
numero_sorteado = random.randrange(0,10)
# Solicita ao usuário que escolha um número entre 0 e 9
numero_escolhido = int(input("Escolha um número de 0 a 9 \n"))
# Determina os números iniciais dos contadores de tentativas
tentativa, numero_invalido = 1, 0
# Compara o número sorteado com o número escolhido pelo usuário
while numero_sorteado != numero_escolhido:
# Ação se o número digitado for inválido
    if numero_escolhido not in range(0,10):
        print("\nNúmero inválido")
        numero_escolhido = int(input("Escolha um número de 0 a 9 \n"))
        numero_invalido += 1
# Ação se o número digitado for válido
    else:
        tentativa += 1
        print("\nErrou, tente de novo")
        numero_escolhido = int(input("\nEscolha um número de 0 a 9 \n"))
# Ação após acertar o número
if numero_invalido == 0:
    print("\nParabéns, você acertou na ", tentativa, "ª tentativa", sep="")
else:
    print("\nParabéns, você acertou depois de ", tentativa + numero_invalido, " tentativas, sendo ", tentativa, " números errados e ", numero_invalido, " números inválidos.", sep="")