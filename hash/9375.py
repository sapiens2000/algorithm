t = int(input())

for i in range(t):
    d = {}
    n = int(input())

    for _ in range(n):
        name, type = input().split()

        if d.get(type):
            d[type] += 1
        else:
            d[type] = 1

    result = 1

    for k in d:
        result *= (d[k]+1)

    print(result - 1)
