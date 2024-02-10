while True:
    #loop will be true until a character N is inserted
    entrada = input("DESEJA SAIR [S] ou [N]")
    sair = entrada.upper().startswith('S')
    if sair:
        break
      
    try:
        numero1=input("INSIRA O NUMERO PARA A OPERAÇÃO ")
        numero2=input("INSIRA O NUMERO PARA A OPERAÇÃO ")
        #If the casting fails, the except will be activated
        numero1=float(numero1)
        numero2=float(numero2)
        
        operador = input("ESCOLHA O OPERADOR + - * / ")
    #condition for choosing the operator
        if operador == '+':
            print(f'{numero1} {operador} {numero2} = {numero1 + numero2}')

        elif operador == '-':
            print(f'{numero1} {operador}  {numero2} = {numero1 - numero2}')

        elif operador == '*':
            print(f'{numero1} {operador}  {numero2} = {numero1 * numero2}')

        elif operador == '/':
            print(f'{numero1} {operador} {numero2} = {numero1 / numero2}')

        else:
            print("OPERADOR INVÁLIDO")


    except:
        print('INSIRA NUMEROS VÁLIDOS')

print('TCHAU')









