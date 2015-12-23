"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt

def summation_of_primes():
	prime_total = 0
	for num in range(1, 2000001):
		if (is_prime(num)):
			prime_total += num
	# subtracting 1 because is_prime considers 1 
	# a prime but Project Euler does not.
	return prime_total - 1 		

def is_prime(number):
	primelist = []
	stop = int(sqrt(number))
	for x in range(1, stop + 1):
		if number % x == 0:
			primelist.append(x)
	if len(primelist) == 1:
		if primelist[0] == 1:
			return True


if __name__ == '__main__':
	summation_of_primes()