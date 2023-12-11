"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Author: Usama Shahid
"""


def multiples_of_3and5(numbers):
    s = 0
    for v in numbers:
        if v % 3 == 0 or v % 5 == 0:
            s += v

    return s


if __name__ == '__main__':
    print(multiples_of_3and5(range(1, 1000)))
