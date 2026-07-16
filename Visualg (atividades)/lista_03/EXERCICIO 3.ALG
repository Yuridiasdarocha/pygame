Algoritmo "EXERCICIO 3"

Var
anos, meses, dias, resultado : inteiro
Inicio
escreva ("Quantos anos? ")
leia (anos)
escreva ("Quantos meses? ")
leia (meses)
se meses >= 13 entao
escreva ("Error: meses não pode ser mais que 12")
senao
escreva ("Quantos dias? ")
leia (dias)
se dias >= 365 entao
escreva ("Error: Dias não pode ser mais que 365")
senao
resultado <- (anos * 365) + (meses * 30) + dias
escreva ("Sua idade expressa apenas em dias é: ",resultado)
fimse
fimse
Fimalgoritmo