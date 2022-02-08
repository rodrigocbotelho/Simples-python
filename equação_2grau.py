from math import sqrt
a = float(input('INFORME O VALOR A: ').strip())
b = float(input('INFORME O VALOR B: ').strip())
c = float(input('INFORME O VALOR C: ').strip())
d = b**2 - 4 * a * c
if d == 0:
    raiz = (-b + sqrt(d)) / (2 * a)
    print('UNICA RAIZ POSSIVEL É: RAIZ = {}'.format(raiz))
else:
    if d < 0:
        print('ESSA EQUAÇÃO NÃO POSSUI NÚMEROS REAIS!')
    else:
        print('RAIZ 1 = {}'.format(-b + sqrt(d)) / (2 * a))
        print('RAIZ 2 = {}'.format(-b - sqrt(d)) / (2 * a))
print('EXIT')