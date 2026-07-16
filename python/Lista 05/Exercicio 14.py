cigarrosdia = int(input("Quantos cigarros você fuma por dia? "))
anosfumando = float(input("Há quantos anos você fuma? "))
totalcigarros = cigarrosdia * (anosfumando * 365)
minutosperdidos = totalcigarros * 10.0
diasperdidos = minutosperdidos / 1440
print (f"Você perdeu aproximadamente {diasperdidos:.2f} dias de vida.")
