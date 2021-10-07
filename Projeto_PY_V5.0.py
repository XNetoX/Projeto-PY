#! python
"""
Windows
Calcular a area de uma circunferencia e imprimir o resultado
pi= math.pi
raio= Entrada do usuario
a=pi*float(raio)**2
"""

# importacoes
import math
import sys

# funcao help


def help():
    print('É necessário informar o raio.')
    print('Sintaxe: {} < raio >'.format(sys.argv[0]))


# if - else
if len(sys.argv) < 2:
    help()
    sys.exit(1)

if not sys.argv[1].isnumeric():
    help()
    print('O valor do raio deve ser númerico')
    sys.exit(2)

# variaveis
pi = math.pi
raio = sys.argv[1]

# funcao


def area(raio):
    return pi*float(raio)**2


# resultado
a = area(raio)
print("Area da circunferencia:", a)
