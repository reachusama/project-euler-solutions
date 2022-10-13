"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Author: Usama Shahid
"""


def largest_palindrome_product():
    def is_palindrome(num):
        n = num
        rev = 0
        while num > 0:
            dig = num % 10
            rev = rev * 10 + dig
            num = num // 10

        return True if n == rev else False

    product = 1
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if is_palindrome(product):
                return product

    return product


if __name__ == '__main__':
    # 580085
    print("largest Palindrom Product: ", largest_palindrome_product())
