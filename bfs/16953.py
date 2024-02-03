from collections import deque

a, b = map(int, input().split())

def bfs():
    q = deque()
    q.append((a, 1))
    cnt = 1

    while q:
        cur, lvl = q.popleft()

        if cur == b:
            print(lvl)
            return

        double = cur * 2
        addOne = cur * 10 + 1

        if double <= b:
            q.append((double, lvl+1))
        if addOne <= b:
            q.append((addOne, lvl + 1))

    print(-1)

bfs()

