#! python
"""
Windows
Calcular a area de uma circunferencia e imprimir o resultado
pi= math.pi
raio= Entrada do usuario
a=pi*raio**2
"""

# importacoes
import math

# variaveis
pi = math.pi
raio = input("Digite o raio:")
a = pi*float(raio)**2

# resultado
print("Area da circunferencia:", a)
