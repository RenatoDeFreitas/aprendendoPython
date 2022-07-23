
varia = input('digite valor qualquer.\n')

def funcao ():
    print(varia)

def pepe2 (arg=None):
    arg = arg.replace('v', 'c')
    # global varia
    # varia = input('digite outro valor\n')
    #print(varia)
    return arg

funcao()
pepe2(arg=varia)


print(varia)
