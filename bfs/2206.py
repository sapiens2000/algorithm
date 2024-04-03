from collections import deque

n, m = map(int, input().split())
mat = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    mat.append(list(map(int, input())))


def check(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True


def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, flag = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][flag]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if check(nx, ny):
                # 벽 아니고 이동 가능한 경우
                if mat[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                    q.append((nx, ny, flag))
                    visited[nx][ny][flag] = visited[x][y][flag] + 1

                # 벽이고 부술수 있는 경우
                elif mat[nx][ny] == 1 and flag == 0:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][0] + 1
    return -1


print(bfs())


