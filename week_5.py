def approx_pi(terms):
	total = 0
	denominator = 3
	for x in range(1,terms):
		if x%2 == 0:
			num1 = 1/float((denominator))
			total += num1
		else: 
			num2 = -(1/float((denominator)))
			total += num2
		denominator += 2
	return 4 * (1 + total)


def pi_sig_digits(decpts):
	if decpts <= 0:
		raise Exception("Accuracy must be positive and non-zero!")
	if isinstance(decpts, int) == False:
		raise Exception("Accuracy must be an integer!") 
	if decpts >= 6:
		raise Exception("Accuracy can only be calculated up to 5 decimal points!")
	total = 0
	a = 0
	b = 0
	y = 0
	z = 0
	x = 1
	accuracy = 0
	while accuracy != 1:
		if x%2 == 0:
			num = 1/float(((2*x)+1))
			total += num
			a = 4 * (1 + total)
			y = int(list(str(a))[decpts + 1])
			final = a
		else: 
			num = -(1/float(((2*x)+1)))
			total += num
			b = 4 * (1 + total)
			z = int(list(str(b))[decpts + 1])
			final = b
		x += 1
		if str(a)[:decpts+1] == str(b)[:decpts+1]:	
			accuracy = abs(y-z)
		
	print "Took {0} tries to calculate pi to an accuracy of of {1} decimal place(s).  Calculated pi is {2}.".format(x, decpts, final)	


# if __name__ == '__main__':
# 	approx_pi(1000000)
# 	pi_sig_digits(3)

