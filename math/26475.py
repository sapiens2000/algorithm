n = int(input())

for _ in range(n):
    d, f, p = input().split()

    if f[0] == '.':
        f = '0' + f
    if p[0] == '.':
        p = '0' + p

    result = round(float(d)*float(f)*float(p), 2)
    print('${:.2f}'.format(result))