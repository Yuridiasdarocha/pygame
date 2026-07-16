Algoritmo "EXERCICIO 3"

Var
km, litros, media : real


Inicio
escreva ("Quantos km você pecorreu? ")
leia (km)
escreva ("Quantos litros você gastou? ")
leia (litros)
se litros > 0 entao
media <- km / litros
escreval ("A média de gasto de litros por km é: ", media)
senao
escreval ("Litros não pode ser = 0")
fimse
Fimalgoritmo