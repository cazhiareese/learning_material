#pyramid

c = 11
counter1 = 1
while counter1 < c:
	counter2 = 0
	while counter2 < c:
		if (c/2) + 4 > (counter1 + counter2) - 1:
			print(' ', end= ' ')
		else:
			print(' * ', end= ' ')
		counter2 = counter2 + 1
	print('\n')
	counter1 = counter1 + 1


#diamond

c = 11
counter1 = 1
while counter1 < c:
	counter2 = 0
	while counter2 < c:
		if (c/2) + 4 > (counter1 + counter2) - 1:
			print(' ', end= ' ')
		else:
			print(' * ', end= ' ')
		counter2 = counter2 + 1
	print('\n')
	counter1 = counter1 + 1
c = 11
counter1 = 1
while counter1 < c:
	counter2 = 0
	while counter2 < c:
		if c- counter2 + counter1 < c :
			print(' * ', end= ' ')
		else:
			print(' ', end= ' ')

		counter2 = counter2 + 1 
	print('\n')
	counter1 = counter1 + 1


#bonus_reversediamond

c = 9	
counter1 = 1
while counter1 < c:
	counter2 = 0
	while counter2 < c*2 -1:
		if counter1 +counter2 +1 > c +counter1 -2 > counter2 or c -counter2 + counter1> c:
			print('*', end= ' ')

		else:
			print(' ', end= ' ')

		counter2 = counter2 + 1 
	print('\n')
	counter1 = counter1 + 1





c = 8
counter1 = 1
while counter1 < c:
	counter2 = 0
	while counter2 < c*2 - counter1 -1:
		if counter1 - 1 < c < counter2 +2 or counter2 + counter1 < c:
			print('*', end= ' ')

		else:
			print(' ', end= ' ')

		counter2 = counter2 + 1 
	print('\n')
	counter1 = counter1 + 1	
