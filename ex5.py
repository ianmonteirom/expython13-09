"""
5. Faça um programa que abra os dois arquivos criados no exercício anterior e copie-os para um novo
arquivo, colocando-os em ordem crescente.
"""

with open('ordem_crescente_numeros.txt', 'w') as arquivo:
    arquivo.write('')

with open('pares.txt', 'r') as arquivo_pares:
    lista_pares = []
    for linha in arquivo_pares:
        lista_pares.append(int(linha))

with open('impares.txt', 'r') as arquivo_impares:
    lista_impares = []
    for linha in arquivo_impares:
        lista_impares.append(int(linha))

lista_total = lista_pares + lista_impares
lista_total.sort()
print(lista_total)

for i in range(len(lista_total)):
    with open('ordem_crescente_numeros.txt', 'a') as arquivo:
        arquivo.write(f'{str(lista_total[i])}\n')

# with open('ordem_crescente.txt', 'w') as arquivo:

with open('ordem_crescente_numeros.txt', 'r') as arquivo:
    print('--' * 40)
    print('Todos os números formatados em forma crescente')
    print(arquivo.read())
