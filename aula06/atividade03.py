for i in range(5):
    print(f'\nVenda {i + 1}')
    valor = float(input('Valor da Compra: '))

    if valor >= 200:
        desconto = valor * 0.10

    else:
        desconto = 0

    valor_final = valor - desconto
    print(f'Valor final: R${valor_final:.2f}')