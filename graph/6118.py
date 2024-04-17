from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * (n+1)
g = [[] * (m+1) for _ in range(n+1)]


def bfs():
    q = deque()
    q.append((1, 0))
    visited[1] = 1

    while q:
        cur, edge = q.popleft()
        for nv in g[cur]:
            if not visited[nv]:
                visited[nv] = visited[cur] + 1
                q.append((nv, edge+1))
    return


for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)


bfs()
length = max(visited)
v = visited.index(length)
count = visited.count(length)
print(v, length-1, count)