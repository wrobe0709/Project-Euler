
def largest_palindrome_product():
	palin_list = []
	for num in range(100000, 998001):
		list_check = []
		for numtxt in str(num):
			list_check.append(numtxt)
		if list_check[0] == list_check[5] and list_check[1] == list_check[4] and list_check[2] == list_check[3]:
			list_check = [''.join(list_check)]
			list_check = int(list_check[0])
			palin_list.append(list_check)

	final_list = []
	for palindrome in palin_list:
		for factor in range(100, 999):
			if palindrome%factor == 0:
				factor_two = (palindrome/factor)
				if len(str(factor_two)) == 3:
					final_list.append(palindrome)
	return max(final_list)

if __name__ == '__main__':
	largest_palindrome_product()
		
	

