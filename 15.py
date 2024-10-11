#15) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

qtd_maca=int(input("Quantas maças você comprou?"))
if qtd_maca <= 6:
    resultado1= qtd_maca*1.30
    print("Suas maçãs são R$:", resultado1)
else:
    resultado2 = qtd_maca*1
    print("Suas maçãs são R$:", resultado2)
