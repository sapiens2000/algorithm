n = int(input())
s = [0]
d = [[0 for _ in range(2)] for _ in range(n+1)]

for _ in range(n):
    s.append(int(input()))

if n == 1:
    print(s[1])
else:
    d[1][0] = s[1]
    d[1][1] = 0
    d[2][0] = s[2]
    d[2][1] = s[1] + s[2]

    for i in range(3, n+1):
        d[i][0] = s[i] + max(d[i-2][0], d[i-2][1])
        d[i][1] = d[i-1][0] + s[i]

    print(max(d[n][0], d[n][1]))
