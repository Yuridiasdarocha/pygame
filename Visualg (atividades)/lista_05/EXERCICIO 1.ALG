Algoritmo "EXERCICIO 1"

Var
valorbruto, valordesconto, preco, desconto, total : real
quantidade : inteiro
nome : caractere

Inicio
escreva ("Qual produto você comprou? ")
leia (nome)
escreva ("Quantas unidades de ",nome," você comprou? ")
leia (quantidade)
escreva ("Qual o preço da unidade de ",nome,"? ")
leia (preco)
se quantidade <= 5 entao
desconto <- 0.02
senao
se quantidade <= 10 entao
desconto <- 0.03
senao
desconto <- 0.05
fimse
fimse

valorbruto <- quantidade * preco
valordesconto <- valorbruto * desconto

total <- valorbruto - valordesconto

escreva ("O valor total a pagar é: ",total)
Fimalgoritmo