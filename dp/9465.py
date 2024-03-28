t = int(input())

for _ in range(t):
    n = int(input())
    nums = []

    dp = [[0 for _ in range(n+1)] for _ in range(2)]

    nums.append(list(map(int, input().split())))
    nums.append(list(map(int, input().split())))

    dp[0][1] = nums[0][0]
    dp[1][1] = nums[1][0]

    for i in range(2, n+1):
        dp[0][i] = nums[0][i-1] + max(dp[1][i-1], dp[0][i-2], dp[1][i-2])
        dp[1][i] = nums[1][i-1] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])

    print(max(dp[0][n], dp[1][n]))


