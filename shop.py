print('=====Loja insana=====')
pre = float(input('Quantos reais voce gastou nesta compra? '))
print('''Como voce deseja realizar este pagamento? 
[ 1 ] - A vista dinheiro/cheque.
[ 2 ] - A vista no cartão.
[ 3 ] - 2x no cartão.
[ 4 ] - 3x ou mais no cartão.''')
opc = int(input('qual a opção? '))
op1 = pre - (pre * 10/100)
op2 = pre - (pre * 5/100)
op3 = pre / 2
op4 = pre + (pre * 20/100)
if opc == 1:
    print(f'o valor total será de {op1:.2f}')
elif opc == 2:
    print(f'o valor total será de {op2:.2f}')
elif opc == 3:
    print(f'o valor será dividido em 2x, sendo: R${op3:.2f}')
    print(f'não há desconto para 2x no cartão, o preço será {pre}')
elif opc == 4:
    x = int(input('quantas parcelas? '))
    z = pre / x
    print(f'o valor a ser pago por mes será de {z:.2f}')
    print(f'o valor total será de {op4:.2f} (+20% de juros)')
else:
    print('Houve um erro, tente novamente.')
