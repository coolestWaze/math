x1 = int(input("digite um valor "))
x2 = int(input("digite o segundo valor "))
x3 = int(input('digite o terceiro valor '))
if x1 < x2 and x1 < x3:
    print(f"o menor número é {x1}")
elif x2 < x1 and x2 < x3:
    print(f"o menor número é {x2}")
elif x3 < x1 and x3 <x2:
    print(f"o menor número é {x3}")
if x1 > x2 and x1 > x3:
    print(f"o maior valor é {x1}")
elif x2 > x1 and x2 > x3:
    print(f"o maior valor é {x2}")
elif x3 > x1 and x3 > x2:
    print(f"o maior número é {x3}")
elif x1 == x2 and x1 == x3:
    print(f"os tres numeros são iguais ({x1} {x2} e {x3})")
elif x2 == x1:
    print(f"tem dois valores iguais ({x2})")
elif x2 == x3:
    print(f"tem dois valores iguais ({x2})")
elif x1 == x2:
    print(f"há dois valores iguais ({x1})")
elif x1 == x3:
    print(f"há dois valores iguais ({x1})")
