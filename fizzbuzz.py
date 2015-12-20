"""
The fizzbuzz function loops through a range of numbers,
set by 'limit', and prints fizzbuzz if 'numOne' and 
'numTwo' are multiples of the current number in the loop.
If only 'numOne' is a multiple the function prints fizz,
if only 'numTwo' is a multiple the function prints buzz.
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