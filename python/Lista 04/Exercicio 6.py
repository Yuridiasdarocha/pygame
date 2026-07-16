idadehomem1 = int(input("Qual a idade do primeiro homem? "))
idadehomem2 = int(input("Qual a idade do segundo homem? "))
idademulher1 = int(input("Qual a idade da primeira mulher? "))
idademulher2 = int(input("Qual a idade da segunda mulher? "))
if (idadehomem1 > idadehomem2) and (idademulher1 > idademulher2):
    soma1 = idadehomem1 + idademulher2
    soma2 = idadehomem2 + idademulher1
else:
    soma1 = idadehomem2 + idademulher1
    soma2 = idadehomem1 + idademulher2
print (f"A soma do homem mais velho com a mulher mais nova é: {soma1}")
print (f"A soma do homem mais novo com a mulher mais velha é: {soma2}")