
t1 = 1, 'Carla', 6, 9 #tupla

# t2 = 'a', 'b', 'c'
# t3 = t1 + t2
#
# n1, n2, n3, *_, n6 = t3
#
# print(t3)
# print(n6)

print(t1)
t1 = list(t1) #transforma tupla em lista
t1[2] = input('digite algo. ')
n1, n2, n3, *_ = t1 #desempacota valor
if n3.isnumeric():
    print('Parabéns {} é um número.'.format(n3))
else:
    print('{} não é um número.'.format(n3))




