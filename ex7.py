'''
Faça um algoritmo em que o usuário define o tamanho da matriz e a preenche por completo com dados. 
A partir dessa matriz o algoritmo deve criar uma matriz do “tipo transposta”. A matriz transposta é 
obtida a partir da troca ordenada de linhas por colunas (e vice-versa), ou seja, todos os elementos 
de uma linha passam a ser elementos de uma coluna, e todos os elementos de uma coluna passam a ser 
elementos de uma linha. Seja M a matriz original, a transposta é denotada por Mt.
Obrigatório: Utilizar o formato da matriz feita em sala de aula (aula05-exercícios). Não utilizar bibliotecas e funções do python.
'''

n = int(input("Digite a quantidade de Linhas das matrizes: "))
m = int(input("Digite a quantidade de Colunas das matrizes: "))

linhas = [0] * m
matriz = [linhas] * n
matriz_transposta = [linhas] * n

def preenche_matriz(matriz):
    for l in range(len(matriz)):
        linha = []
        for c in range(len(matriz[l])):
            numero = int(input(f"Numero ({l},{c}): "))
            linha.append(numero)
        matriz[l] = linha

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i]) 

preenche_matriz(matriz)
print('Matriz: ')
mostra_matriz(matriz) 

## Transposta
for l in range(len(matriz)):
    linha = []
    for c in range(len(matriz[l])):
       linha.append(matriz[c][l])
    matriz_transposta[l] = linha

print('Matriz 3 - Subtração: ')
mostra_matriz(matriz_transposta)