"""
1. Solicite ao usuário 10 números inteiros e armazene-os em um arquivo de texto (um número em cada
linha).
"""

with open('numeros.txt', 'w') as arquivo:
    for i in range(1, 10 + 1):
        n = int(input(f'Digite o {i}o número: '))
        arquivo.write(f'{str(n)}\n')

with open('numeros.txt', 'r') as arquivo:
    print(arquivo.read())
