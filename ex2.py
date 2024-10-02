'''
2 - Faça um algoritmo em que o usuário define o tamanho de duas matrizes e as preenche por completo com dados. 
A partir disso faça a subtração entre as matrizes e armazene em uma terceira matriz. Somente é possível subtrair matrizes de mesmo tamanho.
Obrigatório: Utilizar o formato da matriz feita em sala de aula (aula05-exercícios). Não utilizar bibliotecas e funções do python.
'''

n = int(input("Digite a quantidade de Linhas das matrizes: "))
m = int(input("Digite a quantidade de Colunas das matrizes: "))

linhas = [0] * m
matriz_1 = [linhas] * n
matriz_2 = [linhas] * n
matriz_3 = [linhas] * n

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

print('Matriz 1: ')
preenche_matriz(matriz_1)
print('Matriz 2: ')
preenche_matriz(matriz_2)

print('Matriz 1: ')
mostra_matriz(matriz_1) 

print('Matriz 2: ')
mostra_matriz(matriz_2)

## Subtrai os indices
for l in range(n):
    linha = []
    for c in range(m):
       linha.append(matriz_1[l][c] - matriz_2[l][c])
    matriz_3[l] = linha

print('Matriz 3 - Subtração: ')
mostra_matriz(matriz_3)