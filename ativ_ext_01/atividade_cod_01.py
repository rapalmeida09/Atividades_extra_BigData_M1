"""
- ATIVIDADE COD-01 
Uma loja oferece 16% de desconto nas compras com valor superior a R$ 250.  
Crie um algoritmo, que solicite o valor da compra e informe o valor a ser pago,
após a aplicação do desconto, quando houver.

"""

valor_compra = float(input(f'Informe o valor da compra: '))

if valor_compra >= 250:
    desconto = valor_compra * 0.16
    valor_final = valor_compra - desconto
    print(f'Valor do desconto: R$ {desconto:.2f}')
    print(f'Valor final da compra: R$ {valor_final:.2f}')
else:
    print(f'Valor final da compra: R$ {valor_compra:.2f}')