tipo = input("Qual é a sua instalação? (r -> Residencial, i ->Industrial, c -> Comercial) ")
emc = float(input("Qual é a quantidade em kWh consumida? "))

if tipo == "r":
    print(f"Tem que pagar {round((emc * 0.525),2)} euros")
if tipo == "i":
    print(f"Tem que pagar {round((emc * 0.57),2)} euros")
if tipo == "c":
    print(f"Tem que pagar {round((emc * 0.58),2)} euros")
