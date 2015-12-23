"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt

def pythagorean_triplet():
	for a in range(1, 334):			# a must be less than 333
		for b in range(1, 500):		# b must be less than 499
			c = sqrt((a*a) + (b*b))
			if (c.is_integer()) and (a+b+c == 1000):
				print "a = ", a
				print "b = ", b
				print "c = ", c
				print "product = ", a*b*c

if __name__ == '__main__':
	pythagorean_triplet()

