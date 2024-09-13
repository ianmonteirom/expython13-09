"""
4. Solicite ao usuário diversos números inteiros (até que seja digitado o número zero). Armazene os
números pares em um arquivo e os números ímpares em outro arquivo.
"""

while True:
    try:
        with open('pares.txt', 'r') as arquivo:
            arquivo.read()
    except FileNotFoundError:
        with open('pares.txt', 'w') as arquivo:
            arquivo.write('')

    try:
        with open('impares.txt', 'r') as arquivo:
            arquivo.read()
    except FileNotFoundError:
        with open('impares.txt', 'w') as arquivo:
            arquivo.write('')

    n = int(input('Digite um número (0 interrompe o programa): '))
    if n == 0:
        break
    else:
        if n % 2 == 0:
            n = str(n)
            with open('pares.txt', 'a') as arquivo:
                arquivo.write(f'{n}\n')
        else:
            n = str(n)
            with open('impares.txt', 'a') as arquivo:
                arquivo.write(f'{n}\n')


