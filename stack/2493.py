import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
s = []
result = []

s.append([0, tops[0]])
result.append(0)

for i in range(1, n):
    while s:
        if s[-1][1] > tops[i]:
            result.append(s[-1][0]+1)
            break
        else:
            s.pop()
    if not s:
        result.append(0)
    s.append([i, tops[i]])

print(" ".join(map(str, result)))
