Algoritmo "EXERCICIO 6"

Var
salariofixo, comissao, salariofinal, valorvendas, perc_vendas : real
vendas : inteiro
Inicio
escreva ("Qual seu salário? ")
leia (salariofixo)
escreva ("Qual valor de comissão por cada carro vendido? ")
leia (comissao)
escreva ("Quantos carros você vendeu? ")
leia (vendas)
escreva ("Qual o valor total de vendas? ")
leia (valorvendas)
perc_vendas <- valorvendas * 0.05
salariofinal <- (comissao * vendas) + salariofixo + perc_vendas
escreva ("O valor final do seu salário é: ",salariofinal)
Fimalgoritmo