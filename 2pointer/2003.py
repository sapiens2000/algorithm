n, m = map(int, input().split())
nums = list(map(int, input().split()))
st = 0
en = 0
cnt = 0


while st <= en <= n:
    tmp = sum(nums[st:en])

    if tmp == m:
        cnt += 1
        en += 1
    elif tmp > m:
        st += 1
    elif tmp < m:
        en += 1

print(cnt)
