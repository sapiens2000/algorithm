n = int(input())
arr = list(map(int, input().split()))
prev = arr[0]
diff = 0
result = 0

for num in arr:
    if num > prev:
        diff += num - prev
    else:
        result = max(result, diff)
        diff = 0
    prev = num

print(max(diff, result))