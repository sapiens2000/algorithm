import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
# n + 1 만큼 추가 해서 1에는 기본값 들어가게
# 가로줄 세로줄 초기화 2차원 배열로 가능
d = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        # 해당 칸 값 +
        d[i][j] = board[i-1][j-1] + d[i][j-1] + d[i-1][j] - d[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(d[x2][y2] + d[x1-1][y1-1]-d[x1-1][y2]-d[x2][y1-1])
