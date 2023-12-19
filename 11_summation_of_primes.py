"""
https://projecteuler.net/problem=10
"""
from math import sqrt


def is_prime(n):
    if (n <= 1):
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True


def main():
    s = 0
    for i in range(2000000):
        if is_prime(i):
            s += i
    print(s)


if __name__ == '__main__':
    main()
