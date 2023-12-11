from math import sqrt


def prime_10001st():
    def is_prime(n):
        if (n <= 1):
            return False

        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                return False

        return True

    prime_numbers = []
    i = 1
    while True:
        if len(prime_numbers) == 10001:
            return prime_numbers[-1]

        if is_prime(i):
            prime_numbers.append(i)

        i += 1


if __name__ == '__main__':
    print(prime_10001st())
