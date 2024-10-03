n = s = d = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s+=1
    d+=n
print(f'Voce digitou {s} números e a soma deles é {d}')
