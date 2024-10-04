'''Faça um algoritmo em que o usuário define o tamanho de duas matrizes e as preenche por completo 
com dados. A partir disso faça a transposição da matriz para outra matriz. A transposição de uma matriz
é feita trocando suas linhas por colunas. Ou seja, se a matriz é (m x n) passa a ser (n x m).
Obrigatório: Utilizar o formato da matriz feita em sala de aula (aula05-exercícios). Não utilizar 
bibliotecas e funções do python.
'''

n = int(input("Digite a quantidade de Linhas da matriz: "))
m = int(input("Digite a quantidade de Colunas da matriz: "))

#iniciando as 2 matrizes
matriz = []
for i in range(n):
    linha = [0] * m 
    matriz.append(linha)

matriz_transposta = []
for i in range(m):
    linha_transposta = [0] * n
    matriz_transposta.append(linha_transposta)

def preenche_matriz(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            matriz[l][c] = int(input('Numero ({},{}): '.format(l,c)))

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)

print("Preencha a matriz:")
preenche_matriz(matriz)

#fazendo a transposição da matriz
for i in range(n):
    for j in range(m):
        matriz_transposta[j][i] = matriz[i][j]

print("Matriz Original:")
mostra_matriz(matriz)

print("Matriz Transposta:")
mostra_matriz(matriz_transposta)
