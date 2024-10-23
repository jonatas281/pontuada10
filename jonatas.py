import os 
os. system ("cls || clear")

salario_base=0
depententes=0

def Calcular_inss(salario_base):
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
def Calcular_irrf(salario_base,dependentes):
    salario_com_dependente = salario_base - (dependentes * 189.59)

    match salario_com_dependente:
        case _ if salario_com_dependente <= 2259.20:
            return 0
        case _ if salario_com_dependente <= 2826.65:
            return salario_com_dependente * 0.075
        
        case _ if salario_com_dependente <= 3751.05:
            return salario_com_dependente * 0.15
        
        case _ if salario_com_dependente <= 4664.68:
            return salario_com_dependente * 0.225
        case _:
            return salario_com_dependente * 0.275
def Vale_transporte(salario_base,vale_trasnporte):
     vale_trasnporte == 'sim'
     salario_base * 0.06
     return 0
def Vale_refeicao(vale_refeicao):
     return vale_refeicao *0.20
     
def Plano_saude(dependente):
     return dependente * 150
def Calcular_salario_liquido(salario_base,vale_trasporte,vale_refeicao):
     

    inss = Calcular_inss(salario_base)
    irrf = Calcular_irrf(salario_base,depententes)
    vale_transporte = Vale_transporte (salario_base,vale_trasporte)
    vale_refeicao = Vale_refeicao (vale_refeicao)
    plano_saude = Plano_saude (depententes)

    desconto_total = inss + irrf + vale_transporte + vale_refeicao + plano_saude
    salario_liquido = salario_base - desconto_total

    return salario_liquido, inss, irrf, vale_transporte, vale_refeicao, plano_saude




matricula = int(input("digite sua matricula: "))
senha = int(input("digite sua senha: "))
vale_transporte = input("digite se quer vale transpote: ")
vale_refeicao = float(input("digite o valor do vale refeiçãoda empresa: "))


salario_liquido, inss, irrf, vale_transporte, vale_refeicao, plano_saude = Calcular_salario_liquido (salario_base,vale_transporte,vale_refeicao)

print(f"salario base {salario_base:.2}")
print(f"INSS: R$ {inss:.2f}")
print(f"IRRF: R$ {irrf:.2f}")
print(f"Vale Transporte: R$ {vale_transporte:.2f}")
print(f"Vale Refeição: R$ {vale_refeicao:.2f}")
print(f"Plano de Saúde: R$ {plano_saude:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")


