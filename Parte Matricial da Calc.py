qtd_lin_A = int(input('Quantas Linhas na Matriz A (máx 5):'))
qtd_col_A = int(input('Quantas Colunas na Matriz A (máx 5):'))
matrizA = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for l in range(0, qtd_lin_A):
    for c in range(0, qtd_col_A):
        matrizA[l][c] = int(input(f'Digite um valor para A{l + 1}{c + 1}: '))
print('\n Matriz A: ')
for l in range(0, qtd_lin_A):
    for c in range(0, qtd_col_A):
        print(f'[{matrizA[l][c]}]', end='')
    print()
qtd_lin_B = int(input('Quantas Linhas na Matriz B (máx 5):'))
qtd_col_B = int(input('Quantas Colunas na Matriz B (máx 5):'))
matrizB = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for l in range(0, qtd_lin_B):
    for c in range(0, qtd_col_B):
        matrizB[l][c] = int(input(f'Digite um valor para B{l + 1}{c + 1}: '))
print('\n Matriz B: ')
for l in range(0, qtd_lin_B):
    for c in range(0, qtd_col_B):
        print(f'[{matrizA[l][c]}]', end='')
    print()

if qtd_lin_B == qtd_col_A:
    print('A matriz resultante é:\n ')
    matrizC=[]
    for linha in range(qtd_lin_A):
        matrizC.append([])
        for coluna in range(qtd_col_B):
            matrizC[linha].append(0)
            for k in range(qtd_col_A):
                matrizC[linha][coluna] += matrizA[linha][k] * matrizB[k][coluna]
    qtd_lin_C = len(matrizC)
    qtd_col_C = len(matrizC[0])
    for l in range(0, qtd_lin_C):
        for c in range(0, qtd_col_C):
            print(f'[{matrizC[l][c]}]', end='')
        print()
else:
    print('A quantidade de linhas e colunas das matrizes não possibilita a multiplicação!!!')


#--------------------------------------parte atualizada soma:

qtd_lin_A = int(input('Quantas Linhas na Matriz A (máx 5):'))
qtd_col_A = int(input('Quantas Colunas na Matriz A (máx 5):'))
matrizA = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for l in range(0, qtd_lin_A):
    for c in range(0, qtd_col_A):
        matrizA[l][c] = int(input(f'Digite um valor para A{l + 1}{c + 1}: '))
print('\n Matriz A: ')
for l in range(0, qtd_lin_A):
    for c in range(0, qtd_col_A):
        print(f'[{matrizA[l][c]}]', end='')
    print()
qtd_lin_B = int(input('Quantas Linhas na Matriz B (máx 5):'))
qtd_col_B = int(input('Quantas Colunas na Matriz B (máx 5):'))
matrizB = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for l in range(0, qtd_lin_B):
    for c in range(0, qtd_col_B):
        matrizB[l][c] = int(input(f'Digite um valor para B{l + 1}{c + 1}: '))
print('\n Matriz B: ')
for l in range(0, qtd_lin_B):
    for c in range(0, qtd_col_B):
        print(f'[{matrizB[l][c]}]', end='')
    print()

print('A matriz resultante é:\n ')
matrizC = []
for l in range(max(qtd_lin_A, qtd_lin_B)):
    matrizC.append([])
    for c in range(max(qtd_col_A, qtd_col_B)):
        matrizC[l].append([])
        try:
            matrizC[l][c] = matrizA[l][c] + matrizB[l][c]
        except:
            if matrizA[l][c] < 0 or matrizA[l][c] >= 0:
                matrizC[l][c] = matrizA[l][c]
            else:
                matrizC[l][c] = matrizB[l][c]
for l in range(len(matrizC)):
    for c in range(len(matrizC[0])):
        print(f'[{matrizC[l][c]}]', end='')
    print()
