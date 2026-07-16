Algoritmo "EXERCICIO 8"

Var
maca : inteiro
preco, valorfinal : real
Inicio
escreva ("Quantas maças você comprou? ")
leia (maca)
se maca <= 0 entao
escreva ("Error: o número de maça tem que ser maior que 0")
senao
se maca <= 11 entao
preco <- 1.30
senao
preco <- 1
fimse
valorfinal <- preco * maca
escreva ("O preço final é: ",valorfinal)
fimse
Fimalgoritmo
