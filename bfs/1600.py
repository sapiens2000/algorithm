from collections import deque

k = int(input())
w, h = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(h)]


def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()


    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]



bfs()
if g[w-1][h-1]:
    print(g[w-1][h-1])
else:
    print(-1)