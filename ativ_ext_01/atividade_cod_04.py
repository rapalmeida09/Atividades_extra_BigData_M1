"""
ATIVIDADE COD-04
Um banco permite que seus clientes realizem saques de até R$ 1.000, desde que haja saldo suficiente na conta. Crie um algoritmo que solicite o valor do saque, verifique se a operação pode ser realizada e atualize o saldo da conta.
O algoritmo deve informar o valor sacado e o saldo atual da conta.

"""

saldo = float(input("Informe o saldo inicial da conta: R$ "))


valor_saque = float(input("Informe o valor do saque desejado: R$ "))


if valor_saque <= 0:
    print("Erro: O valor do saque deve ser maior que zero.")
elif valor_saque > 1000:
    print(f"Erro: O limite de saque é R$ 1.000,00. Você tentou sacar R$ {valor_saque:.2f}.")
elif valor_saque > saldo:
    print(f"Erro: Saldo insuficiente. Saldo disponível: R$ {saldo:.2f}.")
else:

    saldo -= valor_saque
    print(f"\nSaque realizado com sucesso!")
    print(f"Valor sacado: R$ {valor_saque:.2f}")
    print(f"Saldo atual da conta: R$ {saldo:.2f}")
