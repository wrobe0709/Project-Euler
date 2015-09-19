from math import sqrt
primes = []

def is_prime(number):
	primelist = []
	stop = int(sqrt(number))
	for x in range(1, stop + 1):
		if number % x == 0:
			primelist.append(x)
	if len(primelist) == 1:
		if primelist[0] == 1:
			return True

def ten_thousand_and_one_primes():
	check = 1
	while len(primes) <= 10000:
		if is_prime(check) == True:
			primes.append(check)
			check += 2
		else:
			check += 2
	return primes[-1]


if __name__ == '__main__':
	ten_thousand_and_one_primes()