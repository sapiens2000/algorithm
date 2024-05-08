t = int(input())

for case in range(1, t+1):
    result = 0
    l, u, x = map(int, input().split())

    if l <= x <= u:
        result = 0
    elif x < l:
        result = l - x
    elif x > u:
        result = -1

    print(f'#{case} {result}')