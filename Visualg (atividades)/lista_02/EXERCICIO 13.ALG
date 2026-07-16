Algoritmo "EXERCICIO 13"

Var
valorpago, valorcompra, troco : real
Inicio
escreva ("Qual o valor do produto? ")
leia (valorcompra)
escreva ("Qual valor pago? ")
leia (valorpago)
se valorpago = valorcompra entao
escreva ("Não tem troco")
senao
troco <- valorpago - valorcompra
escreva ("O troco é: ", troco)
fimse
Fimalgoritmo