"""
- ATIVIDADE COD-08
Uma loja permite o parcelamento de compras a partir de R$ 100.

Crie um algoritmo que solicite o valor total da compra e informe as condições de pagamento de acordo com o valor.

Considere que:

•	compras a partir de R$ 100 podem ser parceladas;
•	compras acima de R$ 1.000 podem ser parceladas em até 10 vezes sem juros;
•	compras acima de R$ 500 podem ser parceladas em até 5 vezes sem juros;
•	as demais compras elegíveis podem ser parceladas em até 3 vezes sem juros;
•	compras abaixo de R$ 100 devem ser pagas à vista.

"""

valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra < 100:
    print("Compra abaixo de R$ 100: pagamento à vista.")
elif valor_compra > 1000:
    print("Compra parcelada em até 10 vezes sem juros.")
elif valor_compra > 500:
    print("Compra parcelada em até 5 vezes sem juros.")
else:
    print("Compra parcelada em até 3 vezes sem juros.")

