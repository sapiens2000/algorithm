n = int(input())

for _ in range(n):
    arr = input()

    for c in arr.split(' '):
        print(c[::-1], end=' ')
    print()