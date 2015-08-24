def sum_multiples():
	biglist = []
	for num in range(1000):
		if num % 3 == 0 or num % 5 == 0:
			biglist.append(num)
	return sum(biglist)