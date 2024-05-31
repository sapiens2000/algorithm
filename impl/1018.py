
chess = [
    [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
    ],
    [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
    ],
]
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())


res = 64
for k in range(2):
    for i in range(n-8+1):
        for j in range(m-8+1):
            tmp = 0

            for l in range(8):
                for o in range(8):
                    if board[i+l][j+o] != chess[k][l][o]:
                        tmp += 1

            res = min(tmp, res)

print(res)