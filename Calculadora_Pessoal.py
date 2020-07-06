import math
from time import sleep
import calc_defs
#def menu():
while True:
    print('''
    \033[34m[1]-Somar                                        \033[32m[16]-Média Ponderada
    \033[31m[2]-Multiplicar                                  \033[33m[17]-Angulo em Graus para Radianos
    \033[32m[3]-Dividir                                      \033[34m[18]-Decimal / Binário 
    \033[33m[4]-Razões Trigonométricas                       \033[31m[19]-Decimal / Hexaecimal
    \033[34m[5]-Soma de Matrizes                             \033[32m[20]-Decimal / Octonal         
    \033[31m[6]-Multiplicar Matrizes                         \033[33m[21]-Tabuada  
    \033[32m[7]-Multiplicar uma única Matriz                 \033[34m[22]-Equação de 2* Grau
    \033[33m[8]-Raiz Quadrada                                \033[31m[23]-Analise de Triângulo
    \033[34m[9]-Raiz Cubica                                  \033[32m[24]-Ordenar Números
    \033[35m[10]-Logaritimo                                  \033[33m[25]-Potencia [dBm] / [w]
    \033[31m[11]-Fatorial                                    \033[34m[26]-
    \033[32m[12]-Progressão Aritmética                       \033[31m[27]-
    \033[33m[13]-Progressão Geométrica                       \033[32m[28]-
    \033[34m[14]-Sequência de Fibonacci                      \033[33m[29]-
    \033[31m[15]-Média Aritimética                           \033[34m[30]-
                               \033[31m[000]Sair \033[m
    ''')
    print('Digite a operação:')
    opcao = int(input())
    if 1 <= opcao <= 10:
        calc_defs.calc_part0.part(opcao)
    elif 11 <= opcao <= 20:
        calc_defs.calc_part1.part(opcao)
    elif 21 <= opcao <= 30:
        calc_defs.calc_part2.part(opcao)
    elif opcao == '000':
        print('Até Mais')
        break
    else:
        print('Opção inválida')
    sleep(4)
