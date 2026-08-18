"""
- ATIVIDADE COD-06
Uma empresa oferece um bônus aos funcionários de acordo com o valor de suas vendas no mês.

Crie um algoritmo que receba o salário e o valor das vendas e calcule o salário final considerando o bônus.
Quando o valor das vendas for superior a R$ 1.000, o funcionário receberá um bônus de R$ 100. Caso contrário,
receberá um bônus de R$ 20.

Ao final, informe o salário inicial, o bônus recebido e o salário final.

"""

salario = float(input("Digite o salário inicial: R$ "))
vendas = float(input("Digite o valor das vendas no mês: R$ "))


if vendas > 1000:
    bonus = 100
else:
    bonus = 20


salario_final = salario + bonus

print("\n" + "=" * 40)
print("CÁLCULO DO SALÁRIO COM BÔNUS")
print("=" * 40)
print(f"Salário inicial: R$ {salario:.2f}")
print(f"Bônus recebido: R$ {bonus:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")
print("=" * 40)