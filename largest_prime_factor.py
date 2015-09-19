from itertools import *
from math import sqrt

def is_prime(number):
	primelist = []
	stop = int(sqrt(number))
	for x in range(1, stop + 1):
		if number % x == 0:
			primelist.append(x)
	if len(primelist) == 1:
		if primelist[0] == 1:
			return True

def largest_prime_factor(given):
	stop = int(sqrt(given))
	factorlist = []
	for x in islice(range(stop), 1, stop, 2):
		if given % x == 0:
			if is_prime(x) == True:
				factorlist.append(x)
	print max(factorlist)

if __name__ == '__main__':
	largest_prime_factor(600851475143)

	
		

