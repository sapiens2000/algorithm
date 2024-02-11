import sys


nums = []
n = int(input())
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
for num in sorted(nums):
    print(num)
