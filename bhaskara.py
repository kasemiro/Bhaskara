#Bhaskara ax²+bx+c=0
from math import sqrt, pow

print('=' *25)
print('Equação do 2º Grau')
print('=' *25)

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
print('=' *25)

print('{}x² {}x {} = 0'.format(a, b, c))
delta = pow(b,2) -4*a*c
print('Δ = {}'.format(delta))
xi = (-b + sqrt(delta)) / (2*a)
print("x' = {}".format(xi))
xii = (-b - sqrt(delta)) / (2*a)
print('x" = {}'.format(xii))
print('=' *25)
