import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
d = [0] * 100001

for i in range(1, n):
    d[i] = d[i-1] + nums[i]


def check():
    left = right = 0
    result = 200000

    while left <= right < n:
        tmp = d[right] - d[left] + nums[left]

        if tmp < s:
            right += 1
        elif tmp >= s:
            result = min(result, right - left + 1)
            left += 1

    if result > 100000:
        return 0
    else:
        return result

print(check())