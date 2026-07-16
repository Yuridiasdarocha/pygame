idade = int(input("Qual a idade? "))
if idade <= 0:
    print("Idade não pode ser 0 ou menor que 0")
elif idade <= 17:
    print("Você é menor de idade!")
elif idade >= 18:
    print("Você é maior de idade!")
