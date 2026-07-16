Algoritmo "Exercicio 7"

Var
A, B , C : inteiro


Inicio
escreva ("Qual o valor de A: ")
leia (A)
escreva ("Qual o valor de B: ")
leia (B)
escreva ("Qual o valor de C: ")
leia (C)
 se (A > B) e (B > C) entao
      escreva (A, ", ", B, ", ", C)
   senao
      se (A > C) e (C > B) entao
         escreva (A, ", ", C, ", ", B)
      senao
         se (B > A) e (A > C) entao
            escreva (B, ", ", A, ", ", C)
         senao
            se (B > C) e (C > A) entao
               escreva (B, ", ", C, ", ", A)
            senao
               se (C > A) e (A > B) entao
                  escreva (C, ", ", A, ", ", B)
               senao
                  escreva (C, ", ", B, ", ", A)
               fimse
            fimse
         fimse
      fimse
   fimse
Fimalgoritmo