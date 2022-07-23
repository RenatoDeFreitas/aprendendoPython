#
# d1 = {
#     'cahve1': 'xtz125',
#     'cahve2': 'bros160',
#     'cahve3': 'versys350',
# }
# #
# # print(d1.get('str'))
# #
# # print('str' in d1)
# # print((1,2,3,4) in d1.keys())
# # print('bros160' in d1.values()) # checa o valor
#
# # print('O total de chaver é ', len(d1))
# # print()
# # for k in d1.values():
# #     print(k)
# #
# # print()
# #
# # for re in d1.items():
# #     print(re[0], re[1])
#
#
# for k, v in d1.items():
#     print(k, v)
################################################

cadastro = {
    'cliente01': {
        'nome': 'Renato',
        'sobrenome': 'Freitas',
    },
    'cliente02': {
        'nome': 'Pedro',
        'sobrenome': 'Castanha',
    }
}
for clientes_k, clientes_v in cadastro.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
