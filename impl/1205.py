n, score, p = map(int, input().split())

if n:
    nums = list(map(int, input().split()))
    tmp = -1

    if n == p and nums[-1] >= score:
        print(-1)
    else:

        for i in range(n):
            if nums[i] <= score:
                print(i + 1)
                break

else:
    print(1)