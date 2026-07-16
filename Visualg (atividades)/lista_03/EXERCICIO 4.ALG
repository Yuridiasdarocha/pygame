Algoritmo "EXERCICIO 4"

Var
eleitores, brancos, nulos, validos : inteiro
perc_brancos, perc_nulos, perc_validos : real
Inicio
escreva ("Qual o total de eleitores? ")
leia (eleitores)
se eleitores <=0 entao
escreva ("Error: o número de eleitores tem que ser maior que 0")
senao
escreva ("Quando o total de votos em branco? ")
leia (brancos)
escreva ("Qual o total de votos nulos? ")
leia (nulos)
escreva ("Qual o total de votos válidos? ")
leia (validos)

perc_brancos <- (brancos / eleitores) * 100
perc_nulos <- (nulos / eleitores) * 100
perc_validos <- (validos / eleitores) * 100

escreval ("Percentual de votos válidos: ", perc_validos,"%")
escreval ("Percentual de votos nulos: ", perc_nulos,"%")
escreval ("Percentual de votos em branco: ", perc_brancos,"%")
fimse
Fimalgoritmo