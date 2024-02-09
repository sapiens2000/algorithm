x = int(input())

d = [0] * 10000001
trail = [0] * 10000001

for i in range(2, x + 1):
    d[i] = d[i-1] + 1
    trail[i] = i - 1

    if i % 2 == 0 and (d[i] > d[i // 2] + 1):
        d[i] = d[i // 2] + 1
        trail[i] = i // 2

    if i % 3 == 0 and (d[i] > d[i // 3] + 1):
        d[i] = d[i // 3] + 1
        trail[i] = i // 3


print(d[x])

pre = x
while True:
    print(pre, end=' ')
    if pre == 1:
        break
    pre = trail[pre]


