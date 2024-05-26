n = int(input())
arr = []
visited = [False] * n

for _ in range(n):
    arr.append(input())

result = n

for i in range(n):
    if visited[i]:
        continue

    for j in range(i+1, n):
        tmp = arr[j]
        for k in range(len(arr[j])):
            if tmp[k:]+tmp[:k] == arr[i]:
                visited[j] = True
                result -= 1
                break

    visited[i] = True


print(result)