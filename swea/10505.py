T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    mid = sum(arr) // n

    result = 0
    for num in arr:
        if num <= mid:
            result += 1

    print(f'#{test_case} {result}')