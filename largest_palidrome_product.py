def palin_product(limit):
    for to_check in range(limit-1, 101100, -1):
        num = to_check
        rev = 0
        while (num > 0):
            div = num % 10
            rev = rev * 10 + div
            num = num / 10
        if (to_check == rev):
            for divisor in range(999, 100, -1):
                if (to_check % divisor == 0):
                    if (to_check/divisor >= 100 and to_check/divisor <= 999):
                        return to_check

t = int(raw_input())
while t > 0:
    in_num = int(raw_input())
    print palin_product(in_num)
    t -= 1
