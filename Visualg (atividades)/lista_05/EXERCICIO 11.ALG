Algoritmo "EXERCICIO 11"

Var
numero , i , contdivisores, somaprimos : inteiro

Inicio
somaprimos <- 0
para numero de 1 ate 100 faca
se numero > 1 entao
contdivisores <- 0
para i de 1 ate numero faca
se numero % i = 0 entao
contdivisores <- contdivisores + 1
fimse
fimpara
se contdivisores = 2 entao
somaprimos <- somaprimos + numero
fimse
fimse
fimpara
escreval ("A soma de todos os números primos entre 1 a 100 é: ", sdomaprimos)
Fimalgoritmo