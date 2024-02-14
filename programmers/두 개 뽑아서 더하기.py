from itertools import combinations


def solution(numbers):
    selects = list(combinations(numbers, 2))
    answer = set()

    for select in selects:
        a, b = select
        answer.add(a + b)

    return sorted(answer)
