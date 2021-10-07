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

# variaveis
pi = math.pi
raio = input("Digite o raio:")

# funcao


def area(raio):
    return pi*float(raio)**2


# resultado
a = area(raio)
print("Area da circunferencia:", a)
