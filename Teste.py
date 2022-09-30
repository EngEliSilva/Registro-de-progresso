# Exemplo de uso da função Random
import random
print("Teste sua sorte!")
numero = random.randrange(0,10)
escolha = int(input("Digite um número de 0 a 9: \n"))
tentativa = 1
while numero != escolha:
    tentativa += 1
    print(">>>", numero, "<<<")
    print("Errou. Tente de novo")
    escolha = int(input("Digite um número de 0 a 9: \n"))
print("Parabéns, você acertou na ", tentativa, "ª tentativa!", sep="")

# Exemplo de uso do laço "for"
#for x in range(3):
#    numero = random.randrange(0,11)
#    print(numero)