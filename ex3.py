'''
3 - Faça um algoritmo em que o usuário define o tamanho da matriz e a preenche por completo com dados. 
A partir dessa matriz o algoritmo deve criar uma matriz do “tipo diagonal”. A matriz diagonal é quadrada e todos os elementos fora 
da diagonal principal são iguais a 0.
Obrigatório: Utilizar o formato da matriz feita em sala de aula (aula05-exercícios). Não utilizar bibliotecas e funções do python.
'''

n = int(input("Digite a quantidade de Linhas das matrizes: "))
m = int(input("Digite a quantidade de Colunas das matrizes: "))

linhas = [0] * m
matriz = [linhas] * n
matriz_diagonal = [linhas] * n

def preenche_matriz(matriz):
    for l in range(n):
        linha = []
        for c in range(m):
            numero = int(input(f"Numero ({l},{c}): "))
            linha.append(numero)
        matriz[l] = linha

def mostra_matriz(matriz):
    for i in range(0 , n):
        print(matriz[i])  

print('Matriz: ')
preenche_matriz(matriz)

print('Matriz: ')
mostra_matriz(matriz) 

## Isola a diagonal
for l in range(n):
    linha = []
    for c in range(m):
        if l == c: 
            linha.append(matriz[l][c])
        else:
            linha.append(0)
    matriz_diagonal[l] = linha

print('Matriz Diagonal: ')
mostra_matriz(matriz_diagonal)

