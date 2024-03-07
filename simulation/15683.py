import copy

n, m = map(int, input().split())
cctvs = []
board = []

#북동남서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] not in (0, 6):
            cctvs.append((tmp[j], i, j))
        if tmp[j] == 0:
            result += 1
    board.append(tmp)


directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]


def fill(x, y, direction, b):
    for i in direction:
        nx, ny = x, y

        while True:
            nx += dx[i]
            ny += dy[i]

            if not (0 <= nx < n and 0 <= ny < m) or b[nx][ny] == 6:
                break

            if b[nx][ny] != 0:
                continue

            b[nx][ny] = -1


def dfs(depth, board):
    global result

    if depth == len(cctvs):
        count = 0
        for i in board:
            count += i.count(0)
        result = min(result, count)
        return

    tmp = copy.deepcopy(board)
    cctv_num, x, y = cctvs[depth]

    for i in directions[cctv_num]:
        fill(x, y, i, tmp)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(board)


dfs(0, board)
print(result)
