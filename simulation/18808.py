n, m, k = map(int, input().split())
laptop = [[0 for _ in range(m)] for _ in range(n)]
stickers = []

for _ in range(k):
    r, c = map(int, input().split())
    tmp = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(tmp)


def attachable(x, y, sticker):
    r, c = len(sticker), len(sticker[0])

    for i in range(r):
        for j in range(c):
            if laptop[x+i][y+j] == 1 and sticker[i][j] == 1:
                return False
    return True


def insert(x, y, sticker):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                laptop[x+i][y+j] = 1


def rotate(sticker):
    r, c = len(sticker), len(sticker[0])
    tmp = [[0 for _ in range(r)] for _ in range(c)]

    for i in range(c):
        for j in range(r):
            tmp[i][j] = sticker[r-1-j][i]
    return tmp


def solution(sticker):
    for _ in range(4):
        r, c = len(sticker), len(sticker[0])
        for i in range(n-r+1):
            for j in range(m-c+1):
                if attachable(i, j, sticker):
                    insert(i, j, sticker)
                    return
        sticker = rotate(sticker)


for sticker in stickers:
    solution(sticker)


cnt = 0
for i in range(n):
    for j in range(m):
        if laptop[i][j] == 1:
            cnt += 1
print(cnt)
