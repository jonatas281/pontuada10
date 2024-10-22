import os 
os. system ("cls || clear")

print("""
====tabela de salario:==== 
                       
|1|= R$1.100,00
|2|= R$2.203,48
|3|= R$3.305,22
|4|= R$6.433,57
""")

salario=int(input("digite o numero em que corresponde ao seu salario:"))


def calcular_inss(salario_base):
    match salario_base:
        case salario if salario <= 1100.00:
            return salario * 0.075
        case salario if salario <= 2203.48:
            return salario * 0.09
        case salario if salario <= 3305.22:
            return salario * 0.12
        case salario if salario <= 6433.57:
            desconto = salario * 0.14
            return min(desconto, 854.36)
        case _:
            return 854.36