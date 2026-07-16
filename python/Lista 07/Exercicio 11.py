# Pede o CPF até ter 11 dígitos válidos
while True:
    cpf = input("Digite o CPF (sem usar pontos ou traços): ")
    # Confere se tem 11 caracteres
    if len(cpf) == 11:
        sonumeros = True
        # Verifica se são só números
        for caractere in cpf:
            if caractere not in "0123456789":
                sonumeros = False
        if sonumeros == True:
            break
        print ("Erro: Digite apenas números.")
    else:
        print ("Digite exatamente 11 digitos do CPF. ")

# Cálculo do primeiro dígito verificador do CPF
# Cada um dos 9 primeiros dígitos é multiplicado por um peso que vai de 10 a 2
partecima1 = (int(cpf[0])) * 10
partecima2 = (int(cpf[1])) * 9
partecima3 = (int(cpf[2])) * 8
partecima4 = (int(cpf[3])) * 7
partecima5 = (int(cpf[4])) * 6
partecima6 = (int(cpf[5])) * 5
partecima7 = (int(cpf[6])) * 4
partecima8 = (int(cpf[7])) * 3
partecima9 = (int(cpf[8])) * 2
somadigito1 = partecima1 + partecima2 + partecima3 + partecima4 + partecima5 + partecima6 + partecima7 + partecima8 + partecima9
# Aqui usamos a regra do módulo 11: pegamos o resto da divisão por 11
divisao1 = somadigito1 // 11
multiplicar1 = divisao1 * 11
subtracao1 = somadigito1 - multiplicar1
# Se o resto for 0 ou 1, o dígito verificador vale 0; caso contrário vale 11 menos o resto
if (subtracao1 == 1) or (subtracao1 == 0):
    digito1 = 0
else:
    digito1 = 11 - subtracao1     

# Cálculo do segundo dígito verificador do CPF
# Agora usamos os 9 primeiros dígitos mais o primeiro dígito verificador, com pesos de 11 a 2
partebaixo1 = (int(cpf[0])) * 11
partebaixo2 = (int(cpf[1])) * 10
partebaixo3 = (int(cpf[2])) * 9
partebaixo4 = (int(cpf[3])) * 8
partebaixo5 = (int(cpf[4])) * 7
partebaixo6 = (int(cpf[5])) * 6
partebaixo7 = (int(cpf[6])) * 5
partebaixo8 = (int(cpf[7])) * 4
partebaixo9 = (int(cpf[8])) * 3
partebaixo10 = (int(cpf[9])) * 2
somadigito2 = partebaixo1 + partebaixo2 + partebaixo3 + partebaixo4 + partebaixo5 + partebaixo6 + partebaixo7 + partebaixo8 + partebaixo9 + partebaixo10
divisao2 = somadigito2 // 11
multiplicar2 = divisao2 * 11
subtracao2 = somadigito2 - multiplicar2
if (subtracao2 == 1) or (subtracao2 == 0):
    digito2 = 0
else:
    digito2 = 11 - subtracao2

# Compara os dígitos calculados com os dois últimos do CPF informado
if (digito1 == int(cpf[9]) and (digito2 == int(cpf[10]))):
    print ("Seu CPF é válido")
else:
    print ("Cpf não é válido")