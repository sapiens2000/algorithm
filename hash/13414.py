import sys

k, l = map(int, input().split())
d = {}


for i in range(l):
    d[sys.stdin.readline().rstrip()] = i

result = sorted(d.items(), key=lambda x: x[1])

k = min(len(result), k)

for i in range(k):
    print(result[i][0])
