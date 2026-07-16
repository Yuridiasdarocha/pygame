altura = float (input("Qual sua altura? "))
peso = float (input("Qual o seu peso? "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print ("Você está abaixo do peso!")
elif imc >= 18.5: 
    print ("Você está com o peso ideal")
elif imc >=25:
    print ("Você está com sobrepeso")
elif imc >= 30:
    print ("Você está com obesidade")
elif imc >= 40:
    print ("Você está com obesidade grave RISCO DE MORTE!")