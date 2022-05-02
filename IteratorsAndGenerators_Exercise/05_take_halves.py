def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            number = i / 2
            yield number

    def take(n, seq):
        result = []
        for i in seq:
            result.append(i)
            if len(result) == n:
                return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
