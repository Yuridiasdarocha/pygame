Algoritmo "exercício 7"

Var kgmorango, kgmaca, totalkg, precomorango, precomaca, subtotal, desconto, totalapagar : real



Inicio
escreva ("Digite os kg de morango: ")
leia (kgmorango)
escreva ("Digite os kg de maça: ")
leia (kgmaca)
se kgmorango <= 5 entao
precomorango <- kgmorango * 2.50
senao
precomorango <- kgmorango * 2.20
fimse
se kgmaca <= 5 entao
precomaca <- kgmaca * 1.80
senao
precomaca <- kgmaca * 1.50
fimse
subtotal <- precomaca + precomorango
totalkg <- kgmaca + kgmorango
se (totalkg > 8) ou (subtotal > 25) entao
desconto <- subtotal * 0.10
senao
desconto <- 0
fimse
totalapagar <- subtotal - desconto
escreval ("Total de kg: ",totalkg)
escreval ("Subtotal: ", subtotal)
escreval ("Desconto: ", desconto)
escreval ("Total a pagar: R$", totalapagar)


Fimalgoritmo