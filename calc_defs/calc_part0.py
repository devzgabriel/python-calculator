import math


def part(opcao):
    str(opcao)
    if opcao == '1':
        soma = 0
        algoritimos = int(input('Quantos Números Somar?'))
        for q in range(0, algoritimos):
            soma += int(input('Quais: '))
        print('O resultado da soma é: ', soma)

    elif opcao == '2':
        mult = 1
        for q in range(0, int(input('Quantos Números Multiplicar?'))):
            mult = mult * int(input('Quais: '))
        print('O resultado da Multiplicação é: ', mult)

    elif opcao == '3':
        divisao = int(input('Dividendo: ')) / int(input('Divisor: '))
        print('Resultado: ', divisao)

    elif opcao == '4':
        angulo = math.radians(float(input('Qual o ângulo: ')))
        print('Seno:{:.2}, Cosseno:{:.2},  Tangente:{:.2}'.format(math.sin(angulo), math.cos(angulo), math.tan(angulo)))

    elif opcao == '5':
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

    elif opcao == '6':
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
            matrizC = []
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

    elif opcao == '7':

        qtd_lin_matriz1 = int(input('Quantas Linhas(máx 5):'))
        qtd_col_matriz1 = int(input('Quantas Colunas(máx 5):'))
        matriz1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        for l in range(0, qtd_lin_matriz1):
            for c in range(0, qtd_col_matriz1):
                matriz1[l][c] = int(input(f'Digite um valor para A{l+1}{c+1}: '))
        print('\n Matriz A: ')
        for l in range(0, qtd_lin_matriz1):
            for c in range(0, qtd_col_matriz1):
                print(f'[{matriz1[l][c]}]', end='')
            print()
        mult = int(input('Por qual número multiplicar: '))
        for l in range(0, qtd_lin_matriz1):
            for c in range(0, qtd_col_matriz1):
                print(f'[{matriz1[l][c] * mult}]', end='')
            print()

    elif opcao == '8':
        num = float(input('Qual o número: '))
        print('A raiz qudrada de {} é: {:.3}'.format(num, num ** (1 / 2)))

    elif opcao == '9':
        num = float(input('Qual o número: '))
        print('A raiz cubica de {} é: {:.3}'.format(num, num ** (1 / 3)))

    elif opcao == '10':
        base = float(input('Qual a base:'))
        logaritimando = float(input('Qual o logaritimando:'))
        logaritimo = math.log(logaritimando, base)
        print(f'O logaritimo de {logaritimando} é {logaritimo}')
