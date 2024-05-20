t = int(input())
dic = ['a', 'e', 'i', 'o', 'u']


for case in range(1, t+1):
    arr = input().rstrip()
    tmp = []

    for c in arr:
        if c in dic:
            continue
        tmp.append(c)
    result = ''.join(tmp)
    print(f'#{case} {result}')