n = int(input())
arr = list(map(int, input().split()))
s = []

prev = arr[0]
diff = 0
result = 0
for num in arr:
    if num < prev:
        diff += num - prev
    else:
        result = max(res, diff)
        diff = 0


print(max(diff, result))