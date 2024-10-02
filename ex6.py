'''
Faça um algoritmo em que o usuário define o tamanho da matriz e a preenche por completo com dados. 
A partir dessa matriz o algoritmo deve criar uma matriz do “tipo oposta”. A matriz oposta é obtida 
invertendo o sinal de todos os elementos da matriz original.
Obrigatório: Utilizar o formato da matriz feita em sala de aula (aula05-exercícios). Não utilizar bibliotecas e funções do python.
'''

n = int(input("Digite a quantidade de Linhas das matrizes: "))
m = int(input("Digite a quantidade de Colunas das matrizes: "))

linhas = [0] * m
matriz = [linhas] * n
matriz_oposta = [linhas] * n

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
mostra_matriz(matriz)

## Cria a matriz oposta
for l in range(n):
    linha = []
    for c in range(m):
        linha.append(matriz[l][c] * -1)
    matriz_oposta[l] = linha

print('Matriz Oposta: ')
mostra_matriz(matriz_oposta)