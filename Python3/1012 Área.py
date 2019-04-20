aux1 = [input().split()]
a = float(aux1[0][0])
b = float(aux1[0][1])
c = float(aux1[0][2])
TR = (a*c)/2
C = (3.14159*(c**2))
T = ((a+b)/2)*c
Q = b**2
R = a*b
print('TRIANGULO: {:.3f}'.format(TR))
print('CIRCULO: {:.3f}'.format(C))
print('TRAPEZIO: {:.3f}'.format(T))
print('QUADRADO: {:.3f}'.format(Q))
print('RETANGULO: {:.3f}'.format(R))