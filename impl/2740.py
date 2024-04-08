n, m = map(int, input().split())
mat1 = []

for _ in range(n):
    mat1.append(list(map(int, input().split())))

m, k = map(int, input().split())
mat2 = []

for _ in range(m):
    mat2.append(list(map(int, input().split())))

result = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for z in range(m):
            result[i][j] += (mat1[i][z]*mat2[z][j])


for i in range(n):
    for j in range(k):
        print(result[i][j], end=' ')
    print()