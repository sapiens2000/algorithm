n = int(input())
mat = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(y-1, y+9):
        for j in range(x-1, x+9):
            mat[i][j] = 1

result = 0
for arr in mat:
    result += arr.count(1)

print(result)