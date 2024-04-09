n = int(input())
nums = list(map(int, input().split()))
nums.sort()
x = int(input())

left = 0
right = n-1
cnt = 0

while left < right:
    tmp = nums[left] + nums[right]

    if tmp == x:
        cnt += 1
        left += 1
        right -= 1
    elif tmp > x:
        right -= 1
    elif tmp < x:
        left += 1

print(cnt)