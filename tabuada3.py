n = int(input('Digite um valor para saber a tábuada: '))
while True:
    if n <= 0:
        break
    else:
        for num in range(0, 11):
            print(f'{n} x {num} = {n*num}')
    n = int(input('Digite um valor para saber a tábuada: '))
print('Programa de tábuada encerrado! ')
