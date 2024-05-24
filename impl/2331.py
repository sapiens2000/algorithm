a, p = map(int, input().split())
d = []

d.append(a)
loc = 0
while True:
    s = str(d[-1])
    tmp = 0

    for n in s:
        tmp += int(n)**p

    if tmp in d:
        loc = d.index(tmp)
        break
    else:
        d.append(tmp)

print(len(d[:loc]))