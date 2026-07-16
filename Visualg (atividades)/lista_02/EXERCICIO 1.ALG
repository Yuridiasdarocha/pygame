Algoritmo "Exercicio 1"

Var
nota1, nota2, nota3, media : real

Inicio
escreva ("Qual a primeira nota? ")
leia (nota1)
escreva ("Qual a segunda nota? ")
leia (nota2)
escreva ("Qual a terceira nota? ")
leia (nota3)
media <- (nota1 + nota2 + nota3) / 3
se media > 7 entao
escreva ("O aluno foi aprovado!Média= ",media:2:2)
senao
escreva ("O aluno foi reprovado!Média= ",media:2:2)
fimse
Fimalgoritmo