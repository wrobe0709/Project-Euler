"""
Finds the difference between the sum of the squares of the 
first n natural numbers and the square of the sum.
"""

def sum_square_diff(n):
    squares = 0
    sum_square = 0
    for num in range(1, n+1):
        squares += (num*num)
        sum_square += num
    return (sum_square * sum_square - squares)


#sum_square_diff(10000)
t = int(raw_input())
while t > 0:
    in_num = int(raw_input())
    print sum_square_diff(in_num)
    t -= 1
