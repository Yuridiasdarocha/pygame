Algoritmo "EXERCICIO 13"

Var
tulipas, coberturas, pessoas : inteiro
valorchopp, valorpizza, valortotal, valorporpessoa : real


Inicio
escreva ("Digite a quantidade de tulipas de chopp: ")
leia (tulipas)
escreva ("Digite a quantidade de coberturas da pizza: ")
leia (coberturas)
escreva ("Digite a quantidade de pessoas na mesa: ")
leia (pessoas)
valorchopp <- tulipas * 5
valorpizza <- 50 + (coberturas * 2.50)
valortotal <- valorchopp + valorpizza
valorporpessoa <- valortotal / pessoas
escreval ("Valor total da conta: R$ ", valortotal)
escreval ("Valor por pessoa: R$ ",valorporpessoa)


Fimalgoritmo