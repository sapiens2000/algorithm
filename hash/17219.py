import sys

n, m = map(int, input().split())
d = {}


for i in range(n):
    site, pw = sys.stdin.readline().rstrip().split()
    d[site] = pw


for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(d[site])