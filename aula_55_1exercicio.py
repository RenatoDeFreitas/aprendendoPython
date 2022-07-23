"""
1 - criar uma função que exiba uma saudação com parâmetros saudação e nome
"""
#



# def apresentacao (saudacao, nome):
#     print(f'{saudacao} comprimento {nome}')
#
# saudacao = input('digite.\n')
# nome = input('qual o nome\n')
#
# apresentacao(saudacao,nome)
# saud('olá', 'renato')
# saud('bão', 'jão')

"""
2 - criar uma função que recebe 3 número como parâmetro e exiba a some entre eles
"""

# def soma (n1, n2, n3):
#     print(f'A soma de {n1} + {n2} + {n3} é ',( n1 + n2 + n3))
# n1 = int(input('digite n1\n'))
# n2 = int(input('digite n2\n'))
# n3 = int(input('digite n3\n'))
#
# soma(n1, n2, n3)


"""
3 - criar uma função que recebe 2 números. Primeiro valor e o segundo é percentual (%). 
Retorne o valor do primeiro número somado do aumento do percentual do mesmo.
"""

def aumento_percentual (valor, percentual):
    print(f' O valor de {valor} aumentado {percentual}% é igual a', (valor + (valor * percentual / 100)))
    print(f'Somente o precentual é', ((valor * percentual)/100))

valor = float(input('Digite o valor.\n'))
percentual = float(input('quantos porcento?\n'))

aumento_percentual(valor, percentual)
# ap = aumento_percentual(50, 10)
# print( ap)
# ap = aumento_percentual(100, 10)
# print( ap)
# ap = aumento_percentual( 30, 15)
# print( ap)

"""
4 - Se divisível por 3 retorne fizz, se por 5 retorne buzz. 
Se divisível por 5 e por 3 retone FizzBuzz, caso contrário retorne número o número enviado.
"""
# n = int(input('digite valor de n.\n'))
#
# def fb (n):
#     if n % 3 == 0 and n % 5 == 0:
#         return f' fizzbuzz, {n} é divisível por 3 e 5'
#     if n % 5 == 0:
#         return f' buzz, {n} é divisível por 5'
#     if n % 3 == 0:
#         return f' fizz, {n} é divisível por 3 '
#     return n
# print (fb(n))

