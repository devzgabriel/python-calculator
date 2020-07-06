import math

def part(opcao):
    str(opcao)
    if opcao == '11':
        n_fat = int(input('Número para calcular o fatorial: '))
        fat = 1
        m = n_fat
        while m > 0:
            fat *= m
            m -= 1
        print(f'O Fatorial de {n_fat} é: {fat}')

    elif opcao == '12':
        prim_term = int(input('Qual o Primeiro termo: '))
        razao = int(input('Qual a Razão: '))
        n_term = int(input('Quantos termos quer saber: '))
        term = prim_term
        c = 0
        mais = 1
        while mais != 0:
            n_term += mais
            while c < n_term:
                print(term, end='')
                print(',' if c + 1 < n_term else '', end='')
                term += razao
                c += 1
            mais = int(input('\n\n Quer mostrar quantos termos a mais? '))
        print('Fim')

    elif opcao == '13':
        prim_term = int(input('Qual o Primeiro termo: '))
        razao = int(input('Qual a Razão: '))
        n_term = int(input('Quantos termos quer saber: '))
        term = prim_term
        c = 0
        mais = 1
        while mais != 0:
            n_term += mais
            while c < n_term:
                print(term, end='')
                print(',' if c + 1 < n_term else '', end='')
                term *= razao
                c += 1
            mais = int(input('\n\n Quer mostrar quantos termos a mais? '))
        print('Fim')

    elif opcao == '14':
        n_term_f = int(input('Quantos termos da sequência que saber: '))
        v1 = 0
        v2 = 1
        c = 3
        if n_term_f != 0:
            print(f'{v1}, {v2}', end=', ')
            while c <= n_term_f:
                v3 = v1 + v2
                print(f'{v3}', end='')
                print(', ' if c < n_term_f else '', end='')
                v1 = v2
                v2 = v3
                c += 1

    elif opcao == '15':
        soma = 0
        qtd_media = int(input('Quantos números calcular na Média:'))
        if qtd_media != 0:
            print('Quais os Números:')
            for c in range(qtd_media):
                n_media = float(input())
                soma += n_media
            print(f'\n A Média Aritimética é {soma / qtd_media}')
    elif opcao == '16':
        soma = 0
        som_peso = 0
        qtd_media = int(input('Quantos números calcular na Média:'))
        if qtd_media != 0:
            for c in range(qtd_media):
                n_media = float(input('Qual o Número e seu peso:'))
                peso = float(input())
                som_peso += peso
                n_media *= peso
                soma += n_media
            print(f'\n A Média é {soma / som_peso}')

    elif opcao == '17':
        conv = 0
        print('''        [0]Graus para Radianos
                [1]Radianos para Graus''')
        opc = int(input())
        if opc == 0:
            conv = int(input('Qual o Ângulo a ser convertido:'))
            print('Em Radianos: ', math.radians(conv))
        elif opc == 1:
            conv = int(input('Qual o Ângulo a ser convertido:'))
            print('Em Graus: ', math.degrees(conv))

    elif opcao == '18':
        conv = 0
        print('''        [0]Decimal para Binário
        [1]Binário para Decimal''')
        opc = int(input())
        if opc == 0:
            conv = int(input('Qual o Número a ser convertido:'))
            print(bin(conv))
        elif opc == 1:
            conv = int(input('Qual o Número a ser convertido:'), 2)
            print('Em Decimal: ', float(conv))

    elif opcao == '19':
        conv = 0
        print('''          [0]Decimal para Hexadecimal
            [1]Hexadecimal para Decimal''')
        opc = int(input())
        if opc == 0:
            conv = int(input('Qual o Número a ser convertido:'))
            print(hex(conv))
        elif opc == 1:
            conv = int(input('Qual o Número a ser convertido:'), 16)
            print('Em Decimal: ', float(conv))

    elif opcao == '20':
        conv = 0
        print('''        [0]Decimal para Octonal
            [1]Octonal para Decimal''')
        opc = int(input())
        if opc == 0:
            conv = int(input('Qual o Número a ser convertido:'))
            print(oct(conv))
        elif opc == 1:
            conv = int(input('Qual o Número a ser convertido:'), 8)
            print('Em Decimal: ', float(conv))
