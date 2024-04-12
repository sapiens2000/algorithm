import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

st = en = 0
result = int(2e9)

while st <= en < n:
    diff = nums[en] - nums[st]

    if diff < m:
        en += 1
    elif diff >= m:
        result = min(result, diff)
        st += 1

print(result)

