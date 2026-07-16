Algoritmo "exercício 8"

Var
numero1, numero2, adicao, subtracao, multiplicacao, divisao : real

Inicio
escreva ("Primeiro número: ")
leia (numero1)
escreva ("Segundo número: ")
leia (numero2)
adicao <- numero1 + numero2
subtracao <- numero1 - numero2
multiplicacao <- numero1 * numero2
se (numero1 = 0) ou (numero2 = 0)  entao
escreval ("Não foi possível efetuar divisão")
senao
divisao <- numero1 / numero2
escreval ("Divisão: ", divisao)
fimse
escreval ("Adição: ", adicao)
escreval ("Subtração: ", subtracao)
escreval ("Multiplicação: ", multiplicacao)

Fimalgoritmo