valor = float(input('Valor do Ingresso: R$ '))

print('''
[1] - INTEIRA (sem descontos)
[2] - MEIA ENTRADA (50% de desconto)
[3] - PROMOÇÃO (30% de desconto)
''')

desconto = 0
opcao =  int(input('Informe o tipo de entrada: '))

match opcao:
    case 1: 
        print('--- INTEIRA ----')
        desconto = 0

    case 2:
        print('--- MEIA ENTRADA (50% de desconto) ----')
        desconto = valor * 0.50

    case 3:
        print('----PROMOÇÃO (30% de desconto) ----')
        desconto = valor * 0.30

if opcao in [1, 2, 3 ]:
    valor_final = valor - desconto
    print(f'\nPreço: R$ {valor:.2f}')
    print(f'Desconto de: R$ {desconto:.2f}')
    print(f'Total a pagar: R$ {valor_final:.2f}')

else:
    print('*_Erro_* Opção Inválida! ')
