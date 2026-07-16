Algoritmo "EXERCICIO 6"

Var
homem1, homem2, mulher1, mulher2, homemvelho, mulhervelha, homemnovo, mulhernova, soma1, soma2 : inteiro


Inicio

escreva ("Digite a idade do 1º homem: ")
leia (homem1)
escreva ("Digite a idade do 2º homem: ")
leia (homem2)
escreva ("Digite a idade da 1º mulher: ")
leia (mulher1)
escreva ("Digite a idade da 2º mulher: ")
leia (mulher2)
se (homem1 = homem2) ou (mulher1 = mulher2) entao
escreva ("As idade não podem ser iguais")
fimse
se homem1 > homem2 entao
homemvelho <- homem1
homemnovo <- homem2
senao
homemvelho <- homem2
homemnovo <- homem1
fimse
se mulher1 > mulher2 entao
mulhervelha <- mulher1
mulhernova <- mulher2
senao
mulhervelha <- mulher2
mulhernova <- mulher1
fimse
soma1 <- homemvelho + mulhernova
soma2 <- mulhervelha + homemnovo
escreva ("A soma do homem mais velho com a mulher mais nova é: ",soma1)
escreva ("A soma do homem mais novo com a mulher mais velha é: ",soma2)
Fimalgoritmo