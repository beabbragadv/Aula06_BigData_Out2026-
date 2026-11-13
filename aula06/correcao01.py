valor = float(input('Valor do Ingresso: R$ '))

print('''
[1] - INTEIRA (sem descontos)
[2] - MEIA ENTRADA (50% de desconto)
[3] - PROMOÇÃO (30% de desconto)
''')

opcao = int(input('Informe a opção: '))

match opcao:
    case 1:
        print('\nSem desconto')

    case 2:
        print('\nPromoção (50% de desconto)')
        desconto = valor * 0.50

    case 3:
        print('\n Promoção(30% de desconto)')
        desconto = valor * 0.30

    case _:
        print('Opção inválida')

if opcao in [1, 2 , 3]:
    valor_final = valor - desconto
    print(f'Valor a pagar R$ {valor_final}')

else:
    print('Digite uma das opções acima')