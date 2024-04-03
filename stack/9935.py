arr = input()
bomb = input()
s = []
offset = len(bomb)

for i in range(len(arr)):
    s.append(arr[i])

    if ''.join(s[-offset:]) == bomb:
        for _ in range(offset):
            s.pop()

if s:
    print(''.join(s))
else:
    print('FRULA')