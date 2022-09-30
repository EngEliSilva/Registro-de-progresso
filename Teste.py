from cgi import print_arguments
from operator import concat


n1 = input("Digite um número de 0 a 10: ")
n2 = input("Digite outro número de 0 a 10: ")
operacao = input("digite um símbolo de operação matemática: ")
print("Quanto é ", end=" ")
print(n1, end=" ")
print(operacao, end=" ")
print(n2, end=" ")
print("?")
resposta = input()
if(resposta == n1 operacao n2, "Parabens :-)", "Você errou :-/")