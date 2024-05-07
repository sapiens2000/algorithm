mat = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1-1, y2-1):
        for j in range(x1-1, x2-1):
            mat[i][j] = 1

result = 0
for arr in mat:
    result += arr.count(1)

print(result)