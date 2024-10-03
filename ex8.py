'''
Faça um algoritmo em que o usuário define o tamanho de duas matrizes e as preenche por completo com dados. 
A partir disso faça a multiplicação entre as matrizes e armazene em uma terceira matriz. Lembrando que para 
que seja possível fazer a multiplicação de matrizes é necessário que o número de linhas da primeira matriz 
seja igual ao número de colunas da segunda, trate essa exceção no algoritmo. Outro ponto importante na 
multiplicação é que deve-se multiplicar os elementos da linha da primeira matriz pelos elementos da coluna 
da segunda matriz e somar esses produtos. Se as matrizes forem 3x2 e 2x3, multiplicar o 1° elemento da 
linha 1 da primeira matriz pelo 1° elemento da coluna 1 da segunda matriz, somamos ao produto do 2° 
elemento da linha 1 da primeira matriz pelo 2° elemento da coluna 1 da segunda matriz e assim por diante.

o produto é calculado multiplicando os elementos de uma linha da primeira matriz pelos elementos correspondentes da coluna da segunda matriz e somando esses produtos.

'''
matriz_resultado = []

def cria_matriz(linha, coluna):
    linhas = [0] * coluna
    matriz = [linhas] * linha
    return matriz

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

while True:
    try:         
        n = int(input("Digite a quantidade de Linhas da primeira matrize: "))
        m = int(input("Digite a quantidade de Colunas da primeira matrize: "))
        matriz_1 = cria_matriz(n, m)

        n = int(input("Digite a quantidade de Linhas da primeira matrize: "))
        m = int(input("Digite a quantidade de Colunas da primeira matrize: "))
        matriz_2 = cria_matriz(n, m)
        
        if len(matriz_1[0]) != len(matriz_2):
            raise ValueError("O numero de linhas da matriz 1 é diferente do número de colunas da matriz 2!!!")
        else:
            break
           
    except ValueError as ve:
        print(ve)
    
preenche_matriz(matriz_1)
preenche_matriz(matriz_2)

print('Matriz 1')
mostra_matriz(matriz_1)
print('Matriz 2')
mostra_matriz(matriz_2)

for l in range(len(matriz_1)):  # Linha matriz 1
    linha = []
    for c in range(len(matriz_2[0])): # Coluna matriz 2
        soma = 0
        for d in range(len(matriz_1[0])):
            soma += matriz_1[l][d] * matriz_2[d][c]
        linha.append(soma)
    matriz_resultado.append(linha)
            
print('Matriz Resultado')
mostra_matriz(matriz_resultado)