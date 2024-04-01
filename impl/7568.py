n = int(input())
result = []
arr = []

for _ in range(n):
    kg, cm = map(int, input().split())
    arr.append([kg, cm])


for i in range(n):
    rank = 1
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    result.append(rank)


for rank in result:
    print(rank, end=' ')


