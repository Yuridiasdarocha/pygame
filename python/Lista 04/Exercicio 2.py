qntdatual = int(input("Qual a quantidade atual no estoque? "))
qntdmaxima = int(input("Qual a quantidade maxima que o estoque pode ter? "))
qntdminima = int(input("Qual a quantidade minima que o estoque pode ter? "))
media = (qntdmaxima + qntdminima) / 2
if qntdatual >= media:
    print ("Não efetuar compra!")
else:
    print ("Efetuar compra!")