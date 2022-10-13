"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Author: Usama Shahid
"""


def sum_square_difference():
    sum = 0
    sum_of_sq = 0
    for i in range(1, 101):
        sum += i
        sum_of_sq += i ** 2

    return sum ** 2 - sum_of_sq


if __name__ == '__main__':
    # 25164150
    print("Sum of Square: ", sum_square_difference())
