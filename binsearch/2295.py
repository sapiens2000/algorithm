n = int(input())
nums = [int(input()) for _ in range(n)]
two = set()
result = 0

nums.sort()

# 집합에 i + j 저장
for i in range(n):
    for j in range(n):
        two.add(nums[i]+nums[j])


# 이분탐색
def check():
    global result
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            if nums[i] - nums[j] in two:
                result = nums[i]
                return

check()
print(result)