import math


def part(opcao):
    str(opcao)
    if opcao == '21':
        n_tab = int(input('Qual o Número da tabuada:'))
        for t in(1, 10):
            print(f'{t} x {n_tab} = {t*n_tab}')

    elif opcao == '22':
        print('Digite os valores de A,B e C')
        a = float(input('A:'))
        b = float(input('B:'))
        c = float(input('C:'))
        delta = ((b * b) - 4 * a * c) ** (1 / 2)
        resultado1 = (-b + delta) / (2 * a)
        resultado2 = (-b - delta) / (2 * a)
        print(f'As Raizes da Equaçâo são {resultado1} e {resultado2}')

    elif opcao == '23':
        i = input('Retas de triangulo:').split()
        v = [float(i) for i in i]
        v.sort(reverse=True)
        a = v[0]
        b = v[1]
        c = v[2]
        if a >= b + c:
            print('NAO FORMA TRIANGULO')
        elif a ** 2 == b ** 2 + c ** 2:
            print('TRIANGULO RETANGULO')
        elif a ** 2 > b ** 2 + c ** 2:
            print('TRIANGULO OBTUSANGULO')
        elif a ** 2 < b ** 2 + c ** 2:
            print('TRIANGULO ACUTANGULO')
        if a == b == c:
            print('TRIANGULO EQUILATERO')
        elif a == b or b == c or a == b:
            print('TRIANGULO ISOSCELES')

    elif opcao == '24':
        qtd = input('Quantos numeros há:')
        numeros = []
        for n in range(qtd):
            numeros.append(input(f'Digite o {n+1}° valor: '))
        ordem = input('Qual a ordem[C/D]: ').upper()
        if ordem not in 'CD':
            ordem = input('Qual a ordem[C/D]: ').upper()
        elif ordem == 'C':
            print(numeros.sort())
        elif ordem == 'D':
            print(numeros.sort(reverse=True))

    elif opcao == '25':
        conv = 0
        print('''          [0][dBm] para [w]
            [1][w] para [dBm]''')
        opc = int(input())
        if opc == 0:
            conv = int(input('Qual a Potência a ser convertida:'))
            print('Em [w]: ', 0.001 * 10**(conv / 10))
        elif opc == 1:
            conv = int(input('Qual a Potência a ser convertida:'), 16)
            print('Em [dBm]: ', 10 * math.log(conv / 0.001))
