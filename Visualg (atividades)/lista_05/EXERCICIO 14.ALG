Algoritmo "EXERCICIO 14"

Var
cigarrosdia, anofumando, totalcigarros : inteiro
diasperdidos, minutosperdidos : real


Inicio
escreva ("Quantos cigarros fuma por dia? ")
leia (cigarrosdia)
escreva ("Há quantos anos fuma? ")
leia (anofumando)
totalcigarros <- cigarrosdia * (anofumando * 365)
minutosperdidos <- totalcigarros * 10.0
diasperdidos <- minutosperdidos / 1440
escreval ("Você perderá aproximadamente " ,diasperdidos:2:2," dias de vida.")

Fimalgoritmo