print('*********************************')
print('Bem vindo a calculadora master !')
print('*********************************')

x = float(input('Digite o primeiro numero:'))   
operator = input('Digite a operação matemática: ')
y = float(input('Digite o segundo numero:'))   


def calculator_lambda():


      
        operations = {
            '+': lambda x, y: x + y, 
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        
        if operator in operations:
            result = operations[operator](x,y)
            print(f'Resultado: {result}')
        else:
            print('Operador invalido')
   

calculator_lambda()