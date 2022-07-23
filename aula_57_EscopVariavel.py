
#
# def pomp():
#         return True''
#
# var = pomp()
# print(var, type(var))



def divisao (n1, n2):
        if n2 == 0:
                return
        return n1 / n2

n1 = int(input('valor de n1\n'))
n2 = int(input('valor de n2\n'))

divide = divisao(n1, n2)

if divide:
        print(divide)
else:
        print('Conta inválida!')



