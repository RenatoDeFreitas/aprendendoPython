""" 1 - Função 1 receber função 2 e retoranr o valor da função 2
"""

# def fun1 ():
#     return input('digite algo.\n')
#
# def mestre2 (funcao):
#     return funcao()
#
# executando = mestre2(fun1())
# print(executando)

""" 2 - Função 1 recebe Função2 como parâmetro e retorna o valor da função2. Função 1 executa duas funções e
  recebe número diferente de argumentos """

pessoa = input('Quem é vc?\n')


def mestre(funcao, *args, **Kwargs):
    return funcao(*args, **Kwargs)


def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, pessoa)
executando2 = mestre(saudacao, pessoa, saudacao='Bom dia!')
print(executando)
print(executando2)






