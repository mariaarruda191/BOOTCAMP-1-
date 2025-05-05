
# Calculadora_Python_Basica

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("Calculadora simples em Python")
print("Operações disponíveis: +, -, *, /")

a = float(input("Digite o primeiro número: "))
op = input("Digite a operação (+, -, *, /): ")
b = float(input("Digite o segundo número: "))

if op == '+':
    print("Resultado:", soma(a, b))
elif op == '-':
    print("Resultado:", subtrai(a, b))
elif op == '*':
    print("Resultado:", multiplica(a, b))
elif op == '/':
    print("Resultado:", divide(a, b))
else:
    print("Operação inválida")
