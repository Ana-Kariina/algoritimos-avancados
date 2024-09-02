#Comissao por carro vendido
comissao = 700
porcentagem = 1.05 
salario_fixo = int(input("Digite seu salário: "))
qtd_vendas = int(input("Quantas vendas você fez neste mês? "))

acrescimo = qtd_vendas*comissao
resultado = acrescimo*porcentagem

print(f"Neste mês você teve {qtd_vendas} vendas e receberá R$ {resultado:.2f} de comissão, além de seu salário fixo.")
#Mais não entendo strings
