import sys

n = int(sys.stdin.readline())
head, tail = sys.stdin.readline().rstrip().split(sep='*')

for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    same = True

    if len(tmp) < len(head) + len(tail):
        print('NE')
        continue
    for i in range(len(head)):
        if head[i] != tmp[i]:
            same = False

    for i in range(len(tail)):
        if tail[i] != tmp[i-len(tail)]:
            same = False

    if same:
        print('DA')
    else:
        print('NE')
