n1 = int(input('digite um valor inteiro: '))
print('''Escolha alguma destas alternativas:
[ 1 ] converter em binário
[ 2 ] converter em octal
[ 3 ] converter em hexadecimal''')
binario = bin(n1)
hexadecimal = hex(n1)
octal = oct(n1)
opcao = int(input("digite a opção: "))
if opcao == 1:
    print(f'o valor {n1} em binário é {binario [2:]}')
elif opcao == 2:
    print(f'o valor {n1} em octal é {octal [2:]}')
elif opcao == 3:
    print(f'o valor {n1} em hexadecimal é {hexadecimal [2:]}')
else:
    print('Opção invalida, tente novamente.')
