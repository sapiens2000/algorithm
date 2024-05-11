n = int(input())
k = int(input())
nums = []
result = set()

for _ in range(n):
    nums.append(input())

visited = [False] * (n+1)
def dfs(arr):
    if len(arr) == k:
        result.add(''.join(arr))
        return

    for i in range(n):
        if not visited[i]:
            arr.append(nums[i])
            visited[i] = True
            dfs(arr)
            visited[i] = False
            arr.pop()


dfs([])
print(len(result))