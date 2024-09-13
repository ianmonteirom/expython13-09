"""
3. Faça um programa que crie um arquivo de texto denominado “arquivo.txt” e permita que o usuário
grave diversos caracteres nesse arquivo até que seja digitado o caractere “0” (zero).
"""

with open('arquivo.txt', 'w') as arquivo:
    while True:
        c = str(input('Grave um caractere no arquivo (0 finaliza o programa): '))
        if c == '0':
            break
        else:
            arquivo.write(f'{c}\n')
        