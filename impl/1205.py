n, score, p = map(int, input().split())

if n:
    nums = list(map(int, input().split()))

    if n == p and nums[-1] >= score:
        print(-1)
    else:
        tmp = n + 1

        for i in range(n):
            if nums[i] <= score:
                tmp = i + 1
                break
        print(tmp)
else:
    print(1)