import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

ans = 1000000000
level = 0
minH = min(map(min, board))
maxH = max(map(max, board))


for height in range(minH, maxH + 1):
    use = 0
    take = 0

    for j in range(n):
        for k in range(m):
            if board[j][k] > height:
                take += board[j][k] - height
            else:
                use += height - board[j][k]

    if use > take + b:
        continue
    else:
        count = take * 2 + use
        if count <= ans:
            ans = count
            level = height

print(ans, level)
