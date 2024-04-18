from collections import deque, defaultdict

import sys
input = sys.stdin.readline


def bfs(i):
    q = deque()
    q.append(i)
    notCycle = True

    while q:
        cur = q.popleft()

        if visited[cur]:
            notCycle = False
        visited[cur] = True

        for v in g[cur]:
            if not visited[v]:
                q.append(v)

            # if v == cur:
            #     notCycle = False
    return notCycle


case = 0
while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    g = defaultdict(list)
    visited = [False] * (n+1)
    ans = 0
    case += 1

    for _ in range(m):
        st, en = map(int, input().split())
        g[st].append(en)
        g[en].append(st)

    for i in range(1, n+1):
        if visited[i]:
            continue
        elif bfs(i):
            ans += 1

    if ans > 1:
        print("Case %d: A forest of %d trees." % (case, ans))
    elif ans == 1:
        print("Case %d: There is one tree." % case)
    else:
        print("Case %d: No trees." % case)
