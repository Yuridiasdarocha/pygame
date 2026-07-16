horastrabalhadas = float (input("Quantas horas você trabalhou no mês? "))
salariohora = float (input("Qual o seu salário por hora? "))

if horastrabalhadas > 160:
    salariobase = salariohora * 160
    horasextras = horastrabalhadas - 160
    valorextra = horasextras * (salariohora * 1.5)
    salariototal = salariobase + valorextra
else:
    salariototal = horastrabalhadas * salariohora
print (f"O valor final do seu salário é: {salariototal}")
