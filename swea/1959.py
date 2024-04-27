t = int(input())
for case in range(1, t + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = int(-1e9)

    end = len(a)
    if len(a) < len(b):
        end = len(b)
        for i in range(end - n + 1):
            tmp = 0
            for j in range(n):
                tmp += a[j] * b[j+i]
            result = max(tmp, result)
    else:
        for i in range(end - m + 1):
            tmp = 0
            for j in range(m):
                tmp += a[j+i] * b[j]
            result = max(tmp, result)

    print(f'#{case} {result}')
