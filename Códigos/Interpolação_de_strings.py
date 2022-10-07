# Importando biblioteca para usar o comando de limpar a tela
import os
os.system('cls') # limpando a tela antes de começar o programa

ano_atual = int (2022) #definindo ano atual

# Coletando informações do usuário
nome = input("Qual o seu nome?\n")
os.system('cls')
hobby = input("O que você gosta de fazer?\n")
os.system('cls')
idade = int(input("Qual sua idade?\n"))
print ("Já fez aniversário esse ano?")
resposta = int(input("Digite: \n[1] para sim \n[2] para não\n"))


# Cálculo condicional do ano de narcimento
if resposta == 1:
    # Se já fez aniversário esse ano
    nascimento = int(ano_atual - idade)
else:
    # Se não fez aniversário esse ano
    nascimento = int(ano_atual - idade + 1)

# Exibindo resultado final
os.system('cls')
print(f">>>{resposta}<<<")

print(f"Obrigado pelas informações, {nome.title()}.") #exibindo texto fixo + nome do usuário corrigindo as iniciais para maiúscula
print(f"Agora já sei que você nasceu em {nascimento} e gosta de {hobby}.")
