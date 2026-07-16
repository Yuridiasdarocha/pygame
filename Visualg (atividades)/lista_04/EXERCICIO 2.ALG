Algoritmo "EXERCICIO 2"

Var
quantidadeatual, quantidademaxima, quantidademinima, media : real


Inicio
escreva ("Qual a quantidade atual? ")
leia (quantidadeatual)
escreva ("Qual a quantidade máxima? ")
leia (quantidademaxima)
escreva ("Qual a quantidade minima? ")
leia (quantidademinima)
media <- (quantidademaxima + quantidademinima) / 2
escreval ("A média é: ", media)
se quantidadeatual >= media entao
escreval ("Não precisa efetuar compra")
senao
escreval ("Efetuar compra")
fimse

Fimalgoritmo