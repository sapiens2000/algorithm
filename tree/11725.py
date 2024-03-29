from collections import deque

n = int(input())
tree = {}

def bfs():
    q = deque()
    q.append(1)
    parent = [0] * (n + 1)

    while q:
        cur = q.popleft()

        for v in tree[cur]:
            if parent[v] == 0 and v != 1:
                q.append(v)
                parent[v] = cur

    for i in range(2, n+1):
        print(parent[i])


for i in range(1, n+1):
    tree[i] = []

for _ in range(n-1):
    parent, child = map(int, input().split())
    tree[parent].append(child)
    tree[child].append(parent)

bfs()
