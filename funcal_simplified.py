import math
def adicao(a, b):
    return a+b
def sub(a, b):
    return a-b
def multi(a, b):
    return a*b
def sqrt(a):
    return math.sqrt(a)
def div(a, b):
    return a/b
def rest(a, b):
    return a%b
while True:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    print('''Oque deseja fazer com estes números? 
    [ 1 ] - adição
    [ 2 ] - subtração
    [ 3 ] - multiplicação
    [ 4 ] - raiz quadrada (primeiro número)
    [ 5 ] - divisão
    [ 6 ] - resto da divisão
    [ 7 ] - sair da calculadora''')
    act = int(input('Escolha o cálculo: '))
    if act == 1:
        print(adicao(a, b))
    elif act == 2:
        print(sub(a, b))
    elif act == 3:
        print(multi(a, b))
    elif act == 4:
        print(sqrt(a))
        print(sqrt(b))
    elif act == 5:
        print(div(a, b))
    elif act == 6:
        print(rest(a, b))
    elif act == 7:
        break
print('Até a proxima!')
exit()
