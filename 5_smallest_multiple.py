"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Author: Usama Shahid
"""
import sys


def smallest_multiple():
    for n in range(2, sys.maxsize):
        is_ok = True
        for i in range(1, 20):
            if n % i != 0:
                is_ok = False

            if not is_ok:
                break
        if is_ok:
            return n


if __name__ == '__main__':
    # 232792560
    print("Smallest Multiple: ", smallest_multiple())
