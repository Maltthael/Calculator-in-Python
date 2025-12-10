print('*********************************')
print('Bem vindo a calculadora master !')
print('*********************************')




def calculator_lambda():

    try:
        x = float(input('Digite o primeiro numero: '))   
        operator = input('Digite a operação matemática: ')
        y = float(input('Digite o segundo numero: '))   
        operations = {
            '+': lambda x, y: x + y, 
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        
        if operator in operations:
            result = operations[operator](x,y)
            print(f'Resultado: {result}')
        elif  y == 0 and operator == '/':
            print('Erro: Divisão com zero não é permitida.')
            raise ZeroDivisionError
        else:
            print('Operador invalido')
            return
    except ValueError:
        print('Erro: entrada apenas de numeros é permitida.')
    except ZeroDivisionError:
        print('Erro: Divisão com zero não é possivel.')
   
   

calculator_lambda()