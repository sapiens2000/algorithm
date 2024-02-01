"""
처음 BFS를 수행해 대륙 별로 다른 넘버 지정 -> 탐색 시작한 대륙과 도착한 대륙 구별을 위함(다르면 도착)
다음 BFS를 통해 다른 대륙 까지 최단 거리 갱신
"""

from collections import deque

n = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
maps = []
shortest = 100000000

for _ in range(n):
    maps.append(list(map(int, input().split())))


def bfs_search(num):
    global shortest
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if maps[i][j] == num:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] > 0 and maps[nx][ny] != num:
                   shortest = min(shortest, visited[x][y])
                elif maps[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

def bfs_numbering(x, y, num):
    q = deque()
    q.append((x, y))
    maps[x][y] = num

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
                q.append((nx, ny))
                maps[nx][ny] = num


num = 2
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            bfs_numbering(i, j, num)
            num += 1

for i in range(2, num):
    bfs_search(i)

print(shortest)