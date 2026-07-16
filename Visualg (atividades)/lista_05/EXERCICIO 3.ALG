Algoritmo "EXERCICIO 3"

Var
codigo, anonascimento, anoingressado, tempoempresa, idade : inteiro


Inicio
escreva ("Qual seu código da empresa? ")
leia (codigo)
escreva ("Qual seu ano de nascimento? ")
leia (anonascimento)
escreva ("Qual ano você ingressou na empresa? ")
leia (anoingressado)
tempoempresa <- 2026 - anoingressado
idade <- 2026 - anonascimento
// informações
escreval ("Seu tempo de empresa é de:",tempoempresa)
escreval ("Sua idade é de:",idade)
// verificação
se (idade >= 65) ou (tempoempresa >= 30) ou (idade >= 60) e (tempoempresa >= 25) entao
escreval ("Status: Requerer aposentadoria")
senao
escreval ("Status: não requerer aposentadoria")
fimse
Fimalgoritmo