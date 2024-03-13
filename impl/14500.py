n, m = map(int, input().split())
board = []

polys = [
    [
        [1, 1, 1, 1]
    ],
    [
        [1, 1],
        [1, 1]
    ],
    [
        [1, 0],
        [1, 0],
        [1, 1]
    ],
    [
        [0, 1],
        [0, 1],
        [1, 1]
    ],
    [
        [1, 0],
        [1, 1],
        [0, 1]
    ],
    [
        [0, 1],
        [1, 1],
        [1, 0]
    ],
    [
        [1, 1, 1],
        [0, 1, 0]
    ]
]

for _ in range(n):
    board.append(list(map(int, input().split())))


def rotate(poly):
    r, c = len(poly), len(poly[0])
    tmp = [[0 for _ in range(r)] for _ in range(c)]

    for i in range(c):
        for j in range(r):
            tmp[i][j] = poly[r-j-1][i]

    return tmp


def put(x, y, poly):
    r, c = len(poly), len(poly[0])
    tmp = 0

    for i in range(r):
        for j in range(c):
            if poly[i][j] == 1:
                tmp += board[x+i][y+j]
    return tmp


def calculate(poly):
    tmp = 0
    for _ in range(4):
        r, c = len(poly), len(poly[0])

        for i in range(n-r+1):
            for j in range(m-c+1):
                tmp = max(tmp, put(i, j, poly))
        poly = rotate(poly)
    return tmp


def solution():
    cnt = 0
    for poly in polys:
        cnt = max(cnt, calculate(poly))
    print(cnt)

solution()