while True:
    #loop will be true until a character N is inserted
    entrada = input("DO YOU WANT TO LEAVE?[Y] ou [N]")
    sair = entrada.upper().startswith('Y')
    if sair:
        break
      
    try:
        numero1=input("ENTER THE NUMBER FOR THE OPERATION :")
        numero2=input("ENTER THE NUMBER FOR THE OPERATION :")
        #If the casting fails, the except will be activated
        numero1=float(numero1)
        numero2=float(numero2)
        
        operador = input("CHOOSE THE OPERATOR: + , - , * , / \n")
    #condition for choosing the operator
        if operador == '+':
            print(f'{numero1} {operador} {numero2} = {numero1 + numero2}')

        elif operador == '-':
            print(f'{numero1} {operador}  {numero2} = {numero1 - numero2}')

        elif operador == '*':
            print(f'{numero1} {operador}  {numero2} = {numero1 * numero2}')

        elif operador == '/':
            if numero2 ==0:
                print("DIVISION ERROR WITH ZERO \n") 
            print(f'{numero1} {operador} {numero2} = {numero1 / numero2}')
        else:
            print("INVALID OPERATOR")


    except:
        print('ENTER VALID NUMBERS')

print('BYEE')












