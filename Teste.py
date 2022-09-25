from typing import Concatenate


print("Preencha as informações abaixo:")
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
print("Data de nascimento:")
dia = input("dia: ")
mes = input("mês: ")
ano = input("ano: ")
nascimento = (dia, mes, ano)
print(dia, mes, ano)
str