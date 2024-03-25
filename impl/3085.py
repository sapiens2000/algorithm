n = int(input())
board = []
result = 0

dx = [1, 0]
dy = [0, 1]

for _ in range(n):
    board.append(list(input()))


def check():
    global result

    for i in range(n):
        cnt = 1
        # 열 검사
        for j in range(n - 1):
            if board[j][i] == board[j + 1][i]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1

        cnt = 1
        # 행 검사
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1


for i in range(n):
    for j in range(n):
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(result)
