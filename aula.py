# um arquivo chamado "nomearquivo.txt" será criado e aberto para escrita.
arquivo = open('nomearquivo.txt', 'w')

# escreve o valor de uma variável str no arquivo
nome = input('Digite seu nome: ')
arquivo.write(nome + '/n')

# escreve o valor de uma variável int no arquivo (deve converter para str)
idade = int(int('Digite sua idade: '))
arquivo.write(str(idade) + '/n')

# fecha o arquivo e libera a memória
arquivo.close()

# utilizando a instrução with
# o with o arquivo só vai existir dentro do with.

with open('meuarquivo.txt', 'r') as arquivo:
    for linha in arquivo:  # percorre as lihas do arquivo
        print(linha)

# aqui o arquivo já está fechado
