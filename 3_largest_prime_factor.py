"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Author: Usama Shahid
"""
from math import sqrt


def largest_prime_factor(integer):
    def isPrime(n):
        if (n <= 1):
            return False

        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                return False

        return True

    lst = []
    for i in range(2, int(sqrt(integer)) + 1):
        if integer % i == 0 and isPrime(i):
            lst.append(i)

    return lst[-1] if len(lst) > 0 else None


if __name__ == '__main__':
    # Answer 6857
    print("Largest Prime Factor: ", largest_prime_factor(600851475143))
