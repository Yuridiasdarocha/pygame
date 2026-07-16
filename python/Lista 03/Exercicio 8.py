quantasmaca = int(input("Quantas maça você comprou? "))
if quantasmaca < 12:
    maca = 1.30
else:
    maca = 1.0
resultado = quantasmaca * maca
print (f"O valor final da sua compra é de {resultado}.")
