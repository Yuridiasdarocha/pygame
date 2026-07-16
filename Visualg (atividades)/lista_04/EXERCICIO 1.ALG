Algoritmo "EXERCICIO 1"

Var
saldo, debito, credito, saldofinal : real


Inicio
escreva ("Qual o seu saldo? ")
leia (saldo)
escreva ("Qual seu crédito? ")
leia (credito)
escreva ("Qual seu débito? ")
leia (debito)

saldofinal <- (saldo + credito) - debito
escreval ("Seu saldo final é de: ", saldofinal)

se saldofinal >= 0 entao
escreval ("Seu saldo é positivo")
senao
escreval ("Seu saldo é negativo")
fimse
Fimalgoritmo