import math

exit1 = 0
while exit1 == 0:

	mas = []
	stg = []
	stf = []
	sty = []
	print("Функция G - 1, Функция F - 2, Функция Y - 3, Введите число: \n")
	number = int(input())	

	if number == 1:
		i = 0
		sta = input("a:")
		a = float(sta)
		stx = input("x:")
		x = float(stx)
		stx2 = input("x2:")
		x2 = float(stx2)
		stk = input("Количество шагов вычисления:")
		kolshag = float (stk)
		shag = (x2 - x)/kolshag
		if shag > x2:
			print ("Шаг вычисления функции > Области вычисления функции\n")
			continue
		while x <= x2-shag:
			if (-20*pow(a,2)+28*a*x+3*pow(x,2)) == 0:
				print ("Функция не может быть вычислена так как знаменатель не может быть = 0\n")
				exit(0)
			G = 4*(-4*pow(a,2)+a*x+5*pow(x,2))/(-20*pow(a,2)+28*a*x+3*pow(x,2))
			mas.append(G)
			stg = "\t".join([str(i) for i in mas])
			print ('{:2f}\t {:2f}'.format(x,mas[i]))
			i = i + 1
			x = x + shag
		print(stg)
		sh = input("Задайте шаблон для поиска совпадения ")
		sovp = stg.count(sh)
		print('Количество совпадений ' '%d' %sovp)
		minimum = min(mas)
		maximum = max(mas)
		print ('Минимальный элемент ''%2f' %minimum)
		print ('Максимальный элемент ''%2f' %maximum) 	

	elif number == 2:			
		sta = input("a:")
		a = float(sta)
		stx = input("x:")
		x = float(stx)
		stx2 = input("x2:")
		x2 = float(stx2)
		stk = input("Количество шагов вычисления:")
		kolshag = float (stk)
		shag = (x2 - x)/kolshag
		if shag > x2:
			print ("Шаг вычисления функции больше чем область вычисления функции\n")
			continue

		i = 0
		while x <= x2-shag:	
			F = (math.atan(24*pow(a,2)-25*a*x+6*pow(x,2)))
			mas.append(F)
			stf = "\t".join([str(i) for i in mas])
			print ('{:2f}\t {:2f}'.format(x,mas[i]))
			i = i + 1
			x = x + shag

		print(stf)
		sh = input("Задайте шаблон для поиска совпадения")
		sovp = stf.count(sh)
		print('Количество совпадений ' '%d' %sovp)
		minimum = min(mas)
		maximum = max(mas)
		print ('Минимальный элемент ''%2f' %minimum)
		print ('Максимальный элемент ''%2f' %maximum) 	 

	elif number == 3:		
		sta = input("a:")
		a = float(sta)
		stx = input("x:")
		x = float(stx)
		stx2 = input("x2:")
		x2 = float(stx2)
		if a == 0 and x == 0:
			print("\nНевозможно посчитать функцию.")
			continue
		stk = input("Количество шагов вычисления:")
		kolshag = float (stk)
		shag = (x2 - x)/kolshag
		if shag > x2:
			print ("Шаг вычисления функции > Области вычисления функции\n")
			continue
		i= 0
		while x <= x2-shag:	
			Y = (math.log(2*pow(a,2)-7*a*x+6*pow(x,2)+1))
			mas.append(Y)
			sty = "\t".join([str(i) for i in mas])
			print ('{:2f}\t {:2f}'.format(x,mas[i]))
			i = i + 1
			x = x + shag

		print(sty)
		sh = input("Задайте шаблон для поиска совпадения")
		sovp = sty.count(sh)
		print('Количество совпадений ' '%d' %sovp)
		minimum = min(mas)
		maximum = max(mas)
		print ('Минимальный элемент ''%2f' %minimum)
		print ('Максимальный элемент ''%2f' %maximum)

	else:
		print('Такой функции нет \n')	
		
			
	print ("Хотите выйти из программы 1 - да 0 - нет")
	exit1 = int(input())		
	
