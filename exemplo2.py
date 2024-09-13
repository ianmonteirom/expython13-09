with open('cadastro.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)

# ------------------------------------------

with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
    cont = 1
    for linha in arquivo:
        print(f'{cont}: {linha}')
        cont += 1

# ------------------------------------------

with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
    lista = []
    for linha in arquivo:
        lista.append(linha.replace('/n', ''))
    print(lista)

nome = input('Nome: ')
if nome in lista:
    print('Cadastrada')
else:
    print('Não cadastrada')
