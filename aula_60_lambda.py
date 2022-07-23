#
# num01 = int(input('digite número 01\n'))
# num02 = int(input('digite número 02\n'))
#
# # a = lambda x, y: x * y
# #
# # print(a(num01, num02))
#
# p1 = input('Digite p1.\n')
# v1 = float(input('Valor do P1.\n'))
# p2 = input('Digite p2.\n')
# v2 = float(input('Valor do P2.\n'))
# p3 = input('Digite p3.\n')
# v3 = float(input('Valor do P3.\n'))
# p4 = input('Digite p4.\n')
# v4 = float(input('Valor do P4.\n'))


lista = [
    ['p1', 2],
    ['p7', 13],
    ['p3', 9],
    ['p5', 146],
    ['p4', 56],
    ['p2', 87],
    ['p6', 7],
]

# lista.sort(key=lambda item: item[0], reverse=True)  # ordenar a lista
# print(lista)

print(sorted(lista,key=lambda i:i[1]))
