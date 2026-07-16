Algoritmo "EXERCICIO 15"

Var
contador : inteiro
acimadecinco, divisivelportres : inteiro
numerosorteado : inteiro

Inicio
acimadecinco <- 0
divisivelportres <- 0
para contador de 1 ate 20 faca
numerosorteado <- randi (11)
escreval ("Número sorteado: ",numerosorteado)
se numerosorteado > 5 entao
acimadecinco <- acimadecinco + 1
fimse
se numerosorteado mod 3 = 0 entao
divisivelportres <- divisivelportres + 1
fimse
fimpara
escreval ("A quantidade de números acima de 5: ",acimadecinco)
escreval ("A quantidade de números divisivel por três: ",divisivelportres)
Fimalgoritmo