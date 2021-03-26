import math


def factors(n):
    if n <= 0:
        raise ValueError(f'{n} is not a positive integer')
    if n == 1:
        return []

    factors_list = [1]
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            factors_list.append(i)
            if n / i != i:
                factors_list.append(n / i)

    return factors_list


def classify(n):
    sum_of_factors = sum(factors(n))

    if sum_of_factors == n:
        return 'perfect'
    elif sum_of_factors > n:
        return 'abundant'
    else:
        return 'deficient'
