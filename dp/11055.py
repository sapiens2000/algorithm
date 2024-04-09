n = int(input())
nums = list(map(int, input().split()))

d = [num for num in nums]

for i in range(n):
    tmp = d[i]
    for j in range(0, i):
        if nums[j] < nums[i]:
            tmp = max(tmp, d[j] + d[i])
    d[i] = tmp

print(max(d))