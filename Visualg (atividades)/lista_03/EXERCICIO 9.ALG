Algoritmo "EXERCICIO 9"

Var
comeco, fim, duracao : real
Inicio
escreva ("Hora de inicio: ")
leia (comeco)
escreva ("Hora do fim: ")
leia (fim)
se fim >= comeco entao
duracao <- fim - comeco
senao
duracao <- 24 - comeco + fim
fimse
escreva ("Duração do jogo: ",duracao,"horas")
Fimalgoritmo
