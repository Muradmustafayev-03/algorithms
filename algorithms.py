import math


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


def prime_factorization(num):
    result = []
    i = 2
    while i <= num:
        if num % i == 0:
            result.append(i)
            num = num / i
        else:
            i += 1

    return result


def euler_func(num):
    result = 0
    num_pf = prime_factorization(num)
    for i in range(1, num):
        if not set(prime_factorization(i)) & set(num_pf):
            result += 1

    return result


def find_all_divisors(num):
    result = []
    for i in range(1, num):
        if num % i == 0:
            result.append(i)

    return result


def multiples(divisor, ceiling):
    result = []
    for i in range(ceiling):
        if i % divisor == 0:
            result.append(i)

    return result


def fibonacci_sequence(ceiling, start=1):
    current = start
    previous = start

    result = []

    while current < ceiling:
        result.append(current)
        sum = previous + current
        previous = current
        current = sum

    return result


def remove_odds(array):
    i = 0

    while i < len(array):
        if array[i] % 2 != 0:
            array.pop(i)
        else:
            i += 1

    return array


def remove_evens(array):
    i = 0

    while i < len(array):
        if array[i] % 2 == 0:
            array.pop(i)
        else:
            i += 1

    return array




