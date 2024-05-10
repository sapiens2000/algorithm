n = int(input())
visited = [False] * (n+1)
nums = [i for i in range(1, n+1)]


def dfs(arr):
    if len(arr) == n:
        for num in arr:
            print(num, end=' ')
        print()
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(arr)
            arr.pop()
            visited[i] = False

dfs([])