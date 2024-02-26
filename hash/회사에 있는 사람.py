n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()

    if v == 'enter':
        d[k] = v
    else:
        del d[k]

for s in sorted(d.keys(), reverse=True):
    print(s)