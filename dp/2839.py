n = int(input())
d = [0] * 5001

d[3] = 1
d[4] = -1
d[5] = 1


for i in range(6, 5001):
    if d[i-3] > 0 and d[i-5] > 0:
        d[i] = min(d[i-3]+1, d[i-5]+1)
    elif d[i-3] > 0:
        d[i] = d[i-3]+1
    elif d[i-5] > 0:
        d[i] = d[i-5]+1
    else:
        d[i] = -1

print(d[n])