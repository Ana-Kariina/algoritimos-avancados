
#17) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

nascimento = int(input("Digite seu ano de nascimento:"))
resultado = 2024 - nascimento
print(resultado)
if resultado > 16:
    print("Pode votar")
else:
    print("Não vote.")
