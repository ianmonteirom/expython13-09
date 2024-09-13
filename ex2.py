"""
2. Abra o arquivo de texto criado no exercício anterior. Leia o conteúdo do arquivo e mostre o somatório
de todos os números contidos no arquivo.
"""

with open('numeros.txt', 'r') as arquivo:
    soma = 0
    for linha in arquivo:
        soma += int(linha)
        print(f'{linha}')
    print(f'Soma total dos números: {soma}')
