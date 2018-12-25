
from math import log, pow, atan

a = float(input('a '))
x = float(input('x' ))

G = (4*(-4*pow(a,2)+a*x+5*pow(x,2)))/(-20*pow(a,2)+28*a*x+3*pow(x,2))
F = (atan(24*pow(a,2)-25*a*x+6*pow(x,2)))
Y = (log(2*pow(a,2)-7*a*x+6*pow(x,2)+1))

print('G = %.6f' % G)
print('F = %.6f' % F)
print('Y = %.6f' % Y)



