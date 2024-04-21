n = list(input())
s = []

ans = 0
tmp = 1

for i in range(len(n)):
    if n[i] == '(':
        s.append(n[i])
        tmp *= 2
    elif n[i] == '[':
        s.append(n[i])
        tmp *= 3
    elif n[i] == ')':
        if not s or s[-1] != '(':
            ans = 0
            break
        if n[i-1] == '(':
            ans += tmp
        s.pop()
        tmp //= 2

    elif n[i] == ']':
        if not s or s[-1] != '[':
            ans = 0
            break
        if n[i-1] == '[':
            ans += tmp
        s.pop()
        tmp //= 3

if s:
    print(0)
else:
    print(ans)