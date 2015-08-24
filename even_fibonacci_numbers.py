def fib_even():
	bif = range(0,34)
	bif_list = []
	sum_list = []
	for y in bif:
		if y == 0 or bif_list[-1] <= 2178309:
			if y == 0:
				bif_list.append(y)
			elif y == 1:
				bif_list.append(y)
			else:
				num = bif_list[y-1] + bif_list[y-2]
				bif_list.append(num)
	for a in bif_list:
		b = a%2
		if b == 0:
			sum_list.append(a)
	total = sum(sum_list)
	return total