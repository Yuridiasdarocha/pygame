Algoritmo "EXERCICIO 10"

Var
horas_mes, valor_hora : real
 horas_extras : real
salario_base, valor_extra, salario_total : real
Inicio
Escreva ("Horas trabalhadas no mês ")
leia (horas_mes)
Escreva ("Seu salário por hora: ")
leia (valor_hora)
se horas_mes > 160 entao
horas_extras <- horas_mes - 160
salario_base <- 160 * valor_hora
valor_extra <- horas_extras * (valor_hora * 1.5)
salario_total <- salario_base + valor_extra
senao
salario_total <- horas_mes * valor_hora
fimse
escreva ("O valor final do seu salário é: ",salario_total)
Fimalgoritmo
