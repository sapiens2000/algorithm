from collections import deque

n = int(input())
m = int(input())
visited = [0] * (n+1)
g = [[] * (m+1) for _ in range(n+1)]


def bfs(v):
    answer = 0
    q = deque()
    q.append((1, 0))
    visited[1] = 1

    while q:
        cur, edge = q.popleft()
        # 2번 - 친구의 친구
        if edge >= 2: continue
        for nv in g[cur]:
            if not visited[nv]:
                visited[nv] = visited[cur] + 1
                q.append((nv, edge+1))
                answer += 1
    return answer


for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

print(bfs(1))






