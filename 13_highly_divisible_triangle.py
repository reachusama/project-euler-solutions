"""
https://projecteuler.net/problem=12
"""


def count_divisors_efficient(n):
    divisor_count = 0
    i = 1

    # Iterate only up to the square root of n
    while i * i <= n:
        if n % i == 0:
            # If i * i == n, then add only one to count to avoid double counting
            if i * i == n:
                divisor_count += 1
            else:
                # Add 2 for both i and n/i
                divisor_count += 2
        i += 1

    return divisor_count


def main():
    factor = 1
    i = 2
    max_divisor = -1
    while True:
        factor = factor + i
        divisors = count_divisors_efficient(factor)

        if max_divisor < divisors:
            max_divisor = divisors

        if divisors >= 500:
            print("500 Done", factor, divisors, max_divisor)
            break

        i += 1


if __name__ == '__main__':
    main()
