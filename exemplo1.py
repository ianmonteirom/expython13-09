try:
    with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
except FileNotFoundError:
    print('Não foi possível ler o arquivo. Arquivo não encontrado.')
else:
    print(texto)


