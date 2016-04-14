def smallest_multiple(n):
	divider = n
	factor = 1
	remainder = 0

	while remainder == 0 and factor <= n:
		remainder = divider%factor
		if factor == n:
			return divider
		if remainder == 0:
			factor += 1
		elif remainder != 0:
			divider += n
			factor = 1
			remainder = 0
            
t = int(raw_input())
while t > 0:
    in_num = int(raw_input())
    print smallest_multiple(in_num)
    t -= 1
