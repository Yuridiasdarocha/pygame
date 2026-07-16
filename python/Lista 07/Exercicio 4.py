distancia = float(input("Qual a distância você deseja pecorrer? "))
if distancia <= 200:
    valorkm = 0.50
else:
    valorkm = 0.45
resultado = distancia * valorkm
print (f"Valor da passagem: {resultado}")