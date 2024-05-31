n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input())))


size = 2
res = 1

max = min(n, m)
# 정사각형 사이즈를 상한까지 늘려가서 전체 탐색
# 조건 만족시에 최대값 갱신
while size <= max:
    for i in range(n-size+1):
        for j in range(m-size+1):
            if board[i][j] == board[i][j+size-1] == board[i+size-1][j] == board[i+size-1][j+size-1]:
                res = size**2
    size += 1


print(res)