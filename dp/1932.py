n = int(input())
nums = []

for _ in range(n):
    nums.append(list(map(int, input().split())))

dp = [[0 for _ in range(n+1)] for _ in range(n)]
dp[0][1] = nums[0][0]

# dp 배열은 높이는 갖고 열에 1개 더 있음
# 왼쪽 위 오른쪽 위  비교 후 큰 값
for i in range(1, n):
    for j in range(1, i+2):
        dp[i][j] = nums[i][j-1] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))