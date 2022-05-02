def get_primes(numbers):
    for number in numbers:
        if number < 2:
            continue
        if number == 2 or number == 3:
            yield number
        elif not (number % 2 == 0 or number % 3 == 0):
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
