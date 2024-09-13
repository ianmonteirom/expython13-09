with open('cadastro.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        rm = input('RM: ')
        if rm == '':
            break
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        arquivo.write(f'{rm} - {nome} - {str(idade)}\n')

