"""
- ATIVIDADE COD-02
Uma loja oferece desconto de 16% nas compras que atendam a pelo menos uma das condições:
valor superior a R$ 250 ou pagamentorealizado pelo PIX.

Crie um algoritmo que solicite o valor da compra e a forma de pagamento e informe o valor final a pagar.
Considere que, quando uma dessas condições for atendida, o desconto deverá ser aplicado. Caso contrário,
o cliente deverá pagar o valor integral.

"""

valor_compra = float(input(f'Informe o valor da compra: '))
forma_pagamento = input(f'Informe a forma de pagamento: ').upper()

if valor_compra > 250 or forma_pagamento == 'PIX':
    desconto = valor_compra * 0.16
    valor_final = valor_compra - desconto
    print(f'Valor do desconto: R$ {desconto:.2f}')
    print(f'Valor final da compra: R$ {valor_final:.2f}')
else:
    print(f'Valor final da compra: R$ {valor_compra:.2f}')
