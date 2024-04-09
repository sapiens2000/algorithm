n = int(input())
nums = list(map(int, input().split()))

d = [1 for _ in range(n)]
trail = [i-1 for i in range(n)]
s = []
for i in range(n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            if d[i] < d[j] + 1:
                trail[i] = j
            d[i] = max(d[i], d[j]+1)

order = max(d)
print(order)


for i in range(n-1, -1, -1):
    if d[i] == order:
        s.append(nums[i])
        order -= 1

print(*reversed(s))