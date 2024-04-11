a, b = map(int, input().split())
nums = [0]


for i in range(1, 46):
    for j in range(i):
        nums.append(i)

print(sum(nums[a:b+1]))