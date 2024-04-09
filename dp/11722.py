n = int(input())
nums = list(map(int, input().split()))

d = [1 for _ in range(n)]


for i in range(n):
    for j in range(0, i):
        if nums[j] > nums[i]:
            d[i] = max(d[i], d[j]+1)

print(max(d))