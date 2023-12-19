"""
https://projecteuler.net/problem=9
"""
import math


def is_triplet(a, b, c):
    if (a ** 2 + b ** 2) == (c ** 2):
        return True
    return False


def main():
    """
    - Create 3 natural numbers
    - Verify if they are triplets
    - If they are triplets, check if their sum = 1000
    - If so, return product of those
    :return:
    """
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if is_triplet(a, b, c) and (a + b + c == 1000):
                    print(a, b, c)
                    print(a * b * c)
                    return None


if __name__ == '__main__':
    main()
