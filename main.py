#  Copyright (c) 2022. Illia Popov.

import math
import random

MODULUS = None


def set_modulus(_modulus):
    global MODULUS
    MODULUS = _modulus


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extended_euclidean_algorithm(a, b):
    """
    ax + by = gcd (a,b)

    :return: gcd (a, b), x, y
    """
    if a == 0:
        return b, 0, 1
    else:
        _gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return _gcd, y - (b // a) * x, x


def miller_rabin_primality_test(n, k=10):
    if n < 2:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        d = d // 2
        r += 1

    for _ in range(k):

        a = random.randrange(2, n - 1)

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False

            if x == n - 1:
                break
        else:
            return False

    return True


def simple_prime_test(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def modular_multiplicative_inverse(a, m):
    # a*x ≡ 1 mod m; gcd(a, m) = 1
    d = extended_euclidean_algorithm(a, m)[1] % m

    return d


def find_remainder(a, m):
    """
    :return: a mod m
    """
    return a % m


def modular_exponentiation(a, b, m):
    """
    :param a: base
    :param b: exp
    :param m: modulus
    :return: a^b mod m
    """

    if b < 0:
        d = modular_multiplicative_inverse(a, m)
        return modular_exponentiation(d, abs(b), m)

    result = 1

    while b > 0:
        if b % 2 != 0:
            result = result * a

        b = b // 2
        a = (a * a) % m

    return result % m


def solve_equation_euler(a, b, m):
    """
    only if gcd (a, m) = 1
    uses Euler's theorem

    :return: solution of ax ≡ b mod m
    """

    result = (b * modular_exponentiation(a, m - 2, m)) % m
    return result


def solve_equation(a, b, m):
    """
    uses Bézout's identity and extended Euclidean algorithm

    :return: all natural solutions of ax ≡ b mod m
    """

    _gcd, x, y = extended_euclidean_algorithm(a, m)

    if b % _gcd != 0:
        # no solutions
        return None

    only_solution_modulus = m / _gcd

    result = (x * (b / _gcd)) % only_solution_modulus

    return [only_solution_modulus * k + result for k in range(_gcd)]


def generate_primes(a, b, prime_test_type: str = 'miller_rabin'):
    prime_test = None

    if prime_test_type == 'miller_rabin':
        prime_test = miller_rabin_primality_test
    elif prime_test_type == 'simple':
        prime_test = simple_prime_test

    while True:
        n = random.randint(a, b)

        if prime_test(n):
            return n


if __name__ == '__main__':

    print("Input the modulus: ")
    set_modulus(int(input()))

    print("Input params:\n")
    print("a mod m = x: a")
    a = int(input())
    print(find_remainder(a, MODULUS))

    print("a^b mod m = x: a, b")
    a, b = input().split()
    print(modular_exponentiation(int(a), int(b), MODULUS))

    print("a*x ≡ b mod m: a, b")
    a, b = input().split()
    print(solve_equation(int(a), int(b), MODULUS))

    print("Modular multiplicative inverse - a*x≡1 mod m: a")
    a = int(input())
    print(modular_multiplicative_inverse(a, MODULUS))

    print("Input interval for prime number: ")
    a, b = input().split()
    print(generate_primes(int(a), int(b), prime_test_type='miller_rabin'))

