def smallest_multiple():
	divider = 20
	factor = 1
	remainder = 0

	while remainder == 0 and factor <= 20:
		remainder = divider%factor
		if factor == 20:
			return divider
		if remainder == 0:
			factor += 1
		elif remainder != 0:
			divider += 20
			factor = 1
			remainder = 0

if __name__ == '__main__':
	smallest_multiple()
	 



			



