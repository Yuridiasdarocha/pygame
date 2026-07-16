Algoritmo "EXERCICIO 9"

Var
numero, i, contDivisores : inteiro
divisores : caractere

Inicio
contDivisores <- 0
divisores <- ""
escreva("Digite um número inteiro positivo: ")
leia(numero)
se numero <= 1 entao
escreval("O número ", numero, " não é primo.")
senao
para i de 1 ate numero faca
se numero % i = 0 entao
contDivisores <- contDivisores + 1
divisores <- divisores + numpcarac(i) + " "
fimse
fimpara
se contDivisores = 2 entao
escreval("O número ", numero, " É PRIMO!")
senao
escreval("O número ", numero, " NÃO É PRIMO.")
escreval("Ele é divisível por: ", divisores)
fimse
fimse
Fimalgoritmo