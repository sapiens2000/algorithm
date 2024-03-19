for case in range(1, 11):
    n = int(input())
    tmp = input()
    result = 0

    for c in tmp:
        if c != '+':
            result += int(c)

    result = str(result)
    print(f'#{case} {result}')
