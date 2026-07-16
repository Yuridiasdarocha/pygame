Algoritmo "EXERCICIO 5"

Var
combustivel : caractere
litros, precolitro, desconto, precobruto, valordesconto, total : real


Inicio
escreva ("(A) de alcool (G) de gasolina: ")
leia (combustivel)
escreva ("Quantos litros? ")
leia (litros)
se (combustivel = "A") ou(combustivel = "a") entao
precolitro <- 3.90
se litros <= 20 entao
desconto <- 0.03
senao
desconto <- 0.05
fimse
senao
se (combustivel = "G") ou (combustivel = "g") entao
precolitro <- 6.30
se litros <= 20 entao
desconto <- 0.06
fimse
senao
escreval ("Tipo inválido")
desconto <- 0.0
precolitro <- 0.0
fimse
fimse
precobruto <- litros * precolitro
valordesconto <- precobruto * desconto
total <- precobruto - valordesconto
escreval ("Preço bruto: ", precobruto)
escreval ("Valor de desconto: ", valordesconto)
escreval ("Valor final: ", total)
Fimalgoritmo