nome1 = str(input("Qual o nome da primeira pessoa? "))
idade1 = int(input(f"Qual a idade de {nome1}? "))
nome2 = str(input("Qual o nome da segunda pessoa? "))
idade2 = int(input(f"Qual a idade de {nome2}? "))
if idade1 == idade2:
    print (f"A idade de {nome1} e {nome2} são iguais.")
elif idade1 > idade2:
    print (f"{nome1} tem a maior idade!")
else:
    print (f"{nome2} tem a mior idade!")