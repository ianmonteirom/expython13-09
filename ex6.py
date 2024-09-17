"""
6. Um professor armazena em um arquivo de texto uma listagem das notas dos alunos na disciplina,
onde cada linha contém o nome do aluno e os valores de quatro notas.
Escreva um programa que leia esse arquivo e calcule a média de cada aluno.
"""

with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        palavras = linha.replace("\n", "").split(" ")
        notas = []
        for i in range(len(palavras)):
            if '.' in palavras[i]:
                notas.append(float(palavras[i]))
        soma_notas = sum(notas)
        media = soma_notas / 4
        print(linha)
        print(f'Média: {media:.2f}')
        print('--' * 40)

