"""
This program plays the game "Fizzbuzz".  It counts to 100, replacing each
multiple of 5 with the word "fizz", each multiple of 7 with the word "buzz",
and each multiple of both with the word "fizzbuzz".  It uses the modulo
operator (%) to determine if a number is divisible by another.
"""

def fizzbuzz(numOne, numTwo, limit):
	for num in range(1, limit + 1):
		if (num % numOne == 0) and (num % numTwo == 0):
			print "fizzbuzz", num
		elif (num % numOne == 0):
			print "fizz", num
		elif (num % numTwo == 0):
			print "buzz", num

if __name__ == '__main__':
	fizzbuzz(25, 10, 100)