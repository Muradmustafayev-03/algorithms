import math


def prime_factorization(num):
    res = []
    i = 2
    while i <= num:
        if num % i == 0:
            res.append(i)
            num = num / i
        else:
            i += 1

    return res


def euler_func(num):
    res = 0
    num_pf = prime_factorization(num)
    for i in range(1, num):
        if not set(prime_factorization(i)) & set(num_pf):
            res += 1

    return res


def find_all_divisors(num):
    res = []
    for i in range(1, num):
        if num % i == 0:
            res.append(i)

    return res


def is_prime(num):
    if num == 1:
        return False

    elif num % 2 == 0 and num != 2:
        return False

    elif (num * 10) % 10 != 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


def _is_prime_(num):  # more accurate, but works slowly
    try:
        for i in range(2, num):
            if num % i == 0:
                return False
    except TypeError:
        return False

    if num <= 1:
        return False

    return True
