def largest_prime_factor(in_num):
    i = 2
    largest_prime = 2
    # checks up to the square root of in_num
    while i*i <= in_num:
        #checks if i is a factor
        while in_num % i == 0:
            # if i is a factor make it the largest prime factor   
            largest_prime = i
            # as long as i is a factor, repeadlty divide in_num down by i       
            in_num /= i             
        # check the next number
        i += 1
    # if what in_num ends up as is greater than what largest_prime is
    # then set in_num to be the largest prime
    if in_num > largest_prime:
        largest_prime = in_num
    return largest_prime 

t = int(raw_input())
while t > 0:
    in_num = int(raw_input())
    print largest_prime_factor(in_num)
    t -= 1