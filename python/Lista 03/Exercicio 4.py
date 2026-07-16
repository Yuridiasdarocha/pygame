eleitores = int(input("Quantos eleitores teve? "))
validos = int(input("Quantos votos válidos? "))
nulos = int(input("Quantos votos nulos? "))
brancos = int(input("Quantos votos em branco? "))
pvalidos = (validos / eleitores) * 100
pnulos = (nulos / eleitores) * 100
pbrancos = (brancos / eleitores) * 100
print (f"Votos válidos: {pvalidos}%")
print (f"Votos nulos: {pnulos}%")
print (f"Votos em branco: {pbrancos}%")