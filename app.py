print('*********************************')
print('Bem vindo a calculadora master !')
print('*********************************')




def calculator_lambda():

    try: #Handle the problem input errors
       
        x = float(input('Digite o primeiro numero: '))  #Receive the first number
        operator = input('Digite a operação matemática: ')    #Receive the wished operator
        y = float(input('Digite o segundo numero: '))  #Receive the second number  
        
        #Map each operator to its corresponding calculation
        operations = {
            '+': lambda x, y: x + y, 
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        
        #conditions to check if there's any problem and execute the calculation
        if  operator == '/' and y == 0:
            print('Erro: Divisão com zero não é permitida.')
            raise ZeroDivisionError
        elif operator in operations:
            result = operations[operator](x,y)
            print(f'Resultado: {result}')
        else:
            print('Operador invalido')
            return
    except ValueError: #If the user type anything diffrent from numbers
        print('Erro: entrada apenas de numeros é permitida.')
    except ZeroDivisionError: # Raised when dividing by zero
        print('Erro: Divisão com zero não é possivel.')
   
   

calculator_lambda()