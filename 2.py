
from math import log, pow, atan

print('___________________________________')
print('Введите значение переменных:')
a = float(input('a= '))
x = float(input('x= '))
print('___________________________________')
print('Введите номер функции(G - 1; F - 2; Y - 3):')
b = int(input('Номер функции: '))
print('___________________________________')
if b == 1:
   G = (4*(-4*pow(a,2)+a*x+5*pow(x,2)))/(-20*pow(a,2)+28*a*x+3*pow(x,2))
   print('G = %.6f' % G)
elif b == 2:
   F = (atan(24*pow(a,2)-25*a*x+6*pow(x,2)))
   print('F = %.6f' % F)
elif b == 3:
   Y = (log(2*pow(a,2)-7*a*x+6*pow(x,2)+1))
   print('Y = %.6f' % Y)
else:
   print('Введён неверный номер формулы!')
print('__________________________________')




