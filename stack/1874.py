n = int(input())
count = 1
s = []
op = []
check = True


for i in range(n):
    num = int(input())

    while count <= num:
        s.append(count)
        op.append('+')
        count += 1

    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        check = False
        break

if check:
    for i in op:
        print(i)
else:
    print('NO')