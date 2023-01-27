#Calculadora com while

while True:
    print("São permitido os seguintes operadores: (+,-,/,*)")
    numero_1=input('Digite um numero: ')
    numero_2=input('Digite outro numero: ')
    operador= input('Digite o operador: ')

    numeros_validos=None
    num_1_float= 0
    num_2_float= 0


    try:
        num_1_float= float(numero_1)
        num_2_float= float(numero_2)
        numeros_validos=True
    except:
        numeros_validos=None
    
    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    operadores_permitidos= "+-/*"
    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue

    if len(operador)>1:
        print("Digite apenas um operador")
        continue

    print("Realizando conta, aguarde...")
    if operador =='+':
        print(f"Resultado: {num_1_float+num_2_float}")

    elif operador == '-':
        print(f"Resultado: {num_1_float-num_2_float}")

    elif operador == '*':
        print(f"Resultado: {num_1_float*num_2_float}")

    elif operador == '/':
        print(f"Resultado: {num_1_float/num_2_float}")



    sair=input("Deseja sair? aperte [s] para 'sim'").lower().startswith('s')

    if sair is True:
        print("Saindo...")
        break