import sys
input = sys.stdin.readline

n = int(input())
before = list(map(int, input().split()))


after = list(sorted(set(before)))
index = {after[i]:i for i in range(len(after))}

for num in before:
    print(index[num], end=' ')