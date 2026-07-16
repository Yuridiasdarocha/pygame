Algoritmo "EXERCICIO 12"

Var
totalaptos : real
diarianormal : real
diariapromocional : real
arrecadacaopromo : real
arrecadacaonormal : real
diferenca : real

Inicio
totalaptos <- 75
diarianormal <- 292
diariapromocional <- diarianormal * 0.75
arrecadacaopromo <- (totalaptos * 0.80) * diariapromocional
arrecadacaonormal <- (totalaptos * 0.50) * diarianormal
diferenca <- arrecadacaopromo - arrecadacaonormal

escreval ("o valor da diária promocional: R$", diariapromocional)
escreval ("O valor total arrecadado com 80% de ocupação e diária promocional: R$", arrecadacaopromo)
escreval ("O valor da arrecadação normal 50% de ocupação: R$", arrecadacaonormal)
escreval ("Diferença de faturamento (lucro extra): R$", diferenca)

Fimalgoritmo