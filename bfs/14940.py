from collections import deque

n, m = map(int, input().split())
mat = []
visited = [[0 for _ in range(m)] for _ in range(n)]
start_x = 0
start_y = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            start_x = i
            start_y = j
    mat.append(tmp)


def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and mat[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

bfs()
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

for row in visited:
    for i in row:
        print(i, end=' ')
    print()