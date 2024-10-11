#16) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = int(input("Digite sua primeira nota:"))
nota2 = int(input("Digite sua segunda nota:"))
resultado = (nota1+nota2)/2
print(resultado)
if resultado > 6:
    print("Aluno aprovado :D")
else:
    resultado < 6
    print("Aluno reprovado :(")
