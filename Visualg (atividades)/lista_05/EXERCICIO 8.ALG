Algoritmo "EXERCICIO 8"

Var
i : inteiro
nome : caractere
nota : real
nomevencedora : caractere
maiornota : real

Inicio
maiornota <- 0
para i de 1 ate 16 faca
escreval ("Dados da ",i,"º Canditada")
escreva ("Nome: ")
leia (nome)
escreva ("Nota 0 a 10: ")
leia (nota)
fimpara
se nota > maiornota entao
maiornota <- nota
nomevencedora <- nome
fimse
escreval (" A vencedora foi: ",nomevencedora)
escreval ("Nota: ",maiornota)
Fimalgoritmo