import math
x1 = float(input("Qual o valor do x1? "))
x2 = float(input("Qual o valor do x2? "))
y1 = float(input("Qual o valor do y1? "))
y2 = float(input("Qual o valor do y2? "))
d = ((x2 - x1)**2 + (y2 - y1)**2)
d = math.sqrt (d)
print (f"Distancia entre p1 e p2: {d:.2f}")


