n = int(input())
result = n
for _ in range(n):
    arr = input().rstrip()

    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        elif arr[i] in arr[i+1:]:
            result -= 1
            break
print(result)