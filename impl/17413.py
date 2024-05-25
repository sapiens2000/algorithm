arr = list(input())

tmp = []
middle = False
for c in arr:
    if c == ' ':
        if not middle:
            print(''.join(tmp[::-1]), end=' ')
            tmp = []
            continue

    tmp.append(c)
    if c == '<':
        middle = True
        if len(tmp) > 1:
            print(''.join(reversed(tmp[:-1])), end='')
            tmp = ['<']

    if c == '>':
        print(''.join(tmp), end='')
        tmp = []
        middle = False

print(''.join(tmp[::-1]), end=' ')