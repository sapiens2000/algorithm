def solution(n):
    t = []

    while n >= 1:
        t.append(str(n % 3))
        n = n // 3

    return int(''.join(t), 3)
