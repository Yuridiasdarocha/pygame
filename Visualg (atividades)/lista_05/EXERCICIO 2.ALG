Algoritmo "EXERCICIO 2"

Var
n1, n2, n3, media, mediaap : real


Inicio
escreva ("Qual a sua primeira nota? ")
leia (n1)
escreva ("Qual sua segunda nota? ")
leia (n2)
escreva ("Qual sua terceira nota? ")
leia (n3)
escreva ("Qual sua média dos exercícios? ")
leia (media)

mediaap <- (n1 + n2 * 2 + n3 * 3 + media) / 7

se mediaap >= 9.0 entao
escreva ("Seu conceito é A")
senao
se mediaap >= 7.5 entao
escreva ("Seu conceito é B")
senao
se mediaap >= 6.0 entao
escreva ("Seu conceito é C")
senao
escreva ("Seu conceito é D")
fimse
fimse
fimse

Fimalgoritmo