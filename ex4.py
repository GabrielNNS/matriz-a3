'''
4 - Faça um algoritmo em que o usuário define o tamanho da matriz e o algoritmo gera uma matriz do “tipo identidade”. 
É uma matriz quadrada onde todos os elementos da diagonal principal são iguais a 1 e todos os elementos fora dessa 
diagonal são iguais a 0.
Obrigatório: Utilizar o formato da matriz feita em sala de aula (aula05-exercícios). Não utilizar bibliotecas e funções do python.
'''

n = int(input("Digite a quantidade de Linhas das matrizes: "))
m = int(input("Digite a quantidade de Colunas das matrizes: "))

linhas = [0] * m
matriz = [linhas] * n

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])  

## Define a diagonal em 1 e o restante em 0
for l in range(n):
    linha = []
    for c in range(m):
        if l == c: 
            linha.append(1)
        else:
            linha.append(0)
    matriz[l] = linha

print('Matriz Diagonal: ')
mostra_matriz(matriz)