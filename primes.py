"""
generate list of first 50 prime numbers

sqrt()
"""
import math
import time

# functions => arguments/parameters
def is_prime(num):
    op = num - 1
    is_prime = True

    while op > 1:
        if num % op == 0:
            is_prime = False
        op -= 1

    return is_prime

def is_prime2(num):
    op = num - 1

    while op > 1:
        if num % op == 0:
            return False
        op -= 1

    return True


def is_prime2_5(num):
    op = 2

    while op < num:
        if num % op == 0:
            return False
        op += 2

    return True

def is_prime3(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

# this will override the name of above function
# is_prime = False
# print(op)

# print(is_prime2(13))
#is_prime(14)
#is_prime(15)
#is_prime(16)
#is_prime(17)

# start = time.time()
for num in range(1000):
    if is_prime2_5(num):
        print("Number: {} is a prime".format(num))
# print(time.time() - start)