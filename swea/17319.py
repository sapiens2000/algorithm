t = int(input())

for case in range(1, t+1):
    n = int(input())
    arr = list(input())
    result = 'No'

    if n % 2 == 1:
        print(f'#{case} No')
        continue

    for i in range(1, n//2+1):
        if arr[:i] * (n//i) == arr:
            result = 'Yes'
            break

    print(f'#{case} {result}')