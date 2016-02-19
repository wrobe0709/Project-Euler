'''
Re-factored this solution to use arithmetic sequences.
Now it will work for large numbers, rather than
just numbers under 1,000.
'''

def sum_multiples(factor, in_num):
    a_n = (in_num - 1)/factor
    sum_3 = a_n * (a_n + 1) / 2 * factor
    return sum_3
    
t = int(raw_input())
while t > 0:
    in_num = int(raw_input())
    print sum_multiples(3, in_num) + sum_multiples(5, in_num) - sum_multiples(15, in_num)
    t -= 1