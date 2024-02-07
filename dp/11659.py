import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(n-1):
    nums[i+1] = nums[i] + nums[i+1]

nums = [0] + nums

for _ in range(m):
    i, j = map(int, input().split())
    print(nums[j] - nums[i-1])