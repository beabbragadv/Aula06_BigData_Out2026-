
for venda in range(5):
    valor = float(input('Informe o valor da compra: '))

    if valor >= 200:
        desconto = valor * 0.10
    else:
        desconto = 0

    valor_final = valor - desconto

    print(f'Desconto de R$: {desconto}')
    print(f'Total a pagar R$: {valor_final}')
