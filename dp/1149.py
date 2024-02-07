n = int(input())
s = []

for _ in range(n):
    s.append(list(map(int, input().split())))

d = [[0 for _ in range(n)] for _ in range(n)]

d[0][0] = s[0][0]
d[0][1] = s[0][1]
d[0][2] = s[0][2]


for k in range(1, n):
    d[k][0] = min(d[k-1][1], d[k-1][2]) + s[k][0]
    d[k][1] = min(d[k-1][0], d[k-1][2]) + s[k][1]
    d[k][2] = min(d[k-1][0], d[k-1][1]) + s[k][2]

print(min(d[n-1][0], d[n-1][1], d[n-1][2]))