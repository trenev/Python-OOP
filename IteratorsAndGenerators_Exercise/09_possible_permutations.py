from itertools import permutations


def possible_permutations(lst):
    for i in permutations(lst):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]
