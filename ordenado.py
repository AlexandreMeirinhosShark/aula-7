salario = float(input("Qual é o seu ordenado atual? "))
if salario <= 0:
    print("Valor inválido. Tente novamente mais tarde.")
elif salario < 500:
    print("Seu reajuste é de 15%")
elif salario < 1000:
    print("Seu reajuste é 10%")
elif salario < 100000:
    print("Seu reajuste é 5%")
else:
    print("caraca ce ta rico :O | Seu reajuste é de 1%")
