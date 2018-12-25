import math

exit1 = 0
while exit1 == 0:

	print("Функция G - 1, Функция F - 2, Функция Y - 3, Введите число: \n")
	number = int(input())
	a = float (input ("a:"))
	x = float (input ("x:"))
	x2 = float (input("x2:"))
	shag = float (input("Шаг вычисления:"))
	if shag > x2:
		print ("Шаг вычисления функции больше чем область вычисления функции\n")
		continue

	if number == 1:
		while x <= x2:
			if (-20*pow(a,2)+28*a*x+3*pow(x,2)) == 0:
				print ("Функция не может быть вычислена так как знаменатель не может быть = 0\n")
				exit(0)
			G = 4*(-4*pow(a,2)+a*x+5*pow(x,2))/(-20*pow(a,2)+28*a*x+3*pow(x,2))
			print ('{:2f}\t {:2f}'.format(x,G))
			x = x + shag

	elif number == 2:
		a = float (input ("a:"))
		x = float (input ("x:"))
		x2 = float (input("x2:"))
		shag = float (input("Шаг вычисления:"))
		if shag > x2:
			print ("Шаг вычисления функции > Области вычисления функции\n")
			continue
		while x <= x2:	
			F = (atan(24*pow(a,2)-25*a*x+6*pow(x,2)))
			print ('{:2f}\t {:2f}'.format(x,F))
			x = x + shag
			
	elif number == 3:
			a = float (input ("a:"))
			x = float (input ("x:"))
			x2 = float (input("x2:"))
			shag = float (input("Шаг вычисления:"))
			if shag > x2:
				print ("Шаг вычисления функции > Области вычисления функции\n")
				continue
			Y = (log(2*pow(a,2)-7*a*x+6*pow(x,2)+1))
			print ('{:2f}\t {:2f}'.format(x,Y))
			x = x + shag
			
	else:
		print('Такой функции нет \n')

	print ("Хотите выйти из программы 1 - да 0 - нет")
	exit1 = int(input())		
	
