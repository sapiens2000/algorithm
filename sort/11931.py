import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

for num in sorted(arr, reverse=True):
    print(num)