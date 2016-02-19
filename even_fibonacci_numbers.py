'''
Re-factored to work for large inputs.
'''

def even_fib(in_num, prev_1, prev_2, even_sum):
    new_sum = prev_1 + prev_2
    if new_sum < in_num:
        if new_sum % 2 == 0:
            even_sum += new_sum
        return even_fib(in_num, prev_2, new_sum, even_sum)
    else:
        return even_sum + 2

t = int(raw_input())
while t > 0:
    in_num = int(raw_input())
    print even_fib(in_num, 1, 2, 0)
    t -= 1