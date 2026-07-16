Algoritmo "EXERCICIO 10"

Var
lado1, lado2, lado3 : real

Inicio
escreva ("Primeiro lado: ")
leia (lado1)
escreva ("Segundo lado: ")
leia (lado2)
escreva ("Terceiro lado: ")
leia (lado3)
se (lado1 < lado2 + lado3) e (lado2 < lado1 + lado3) e (lado3 < lado1 + lado2) entao
se (lado1 = lado2) e (lado2 = lado3) entao
escreva ("O triângulo é Equilátero todos os lados iguais")
senao
se (lado1 <> lado2) e (lado2 <> lado3) e (lado1 <> lado3) entao
escreva ("O triângulo é escaleno todos os lados diferentes")
senao
escreva ("O triângulo é isósceles dois lados iguais e um diferente")
fimse
fimse
senao
escreva ("Não é possível formar um triângulo")
fimse
Fimalgoritmo