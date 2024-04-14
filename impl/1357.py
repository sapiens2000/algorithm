n, m = map(int, input().split())


def reverse(num):
    return int(str(num)[::-1])


print(reverse(reverse(n) + reverse(m)))

