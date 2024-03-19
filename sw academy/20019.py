t = int(input())


for k in range(1, t+1):
    stack = []
    s = input()
    flag = True

    if s == s[::-1]:
        head = s[:len(s)//2]
        tail = s[len(s)//2+1:]

        if head != head[::-1]:
            flag = False

        if tail != tail[::-1]:
            flag = False

        if flag:
            print('#' + str(k) + ' YES')
        else:
            print('#' + str(k) + ' NO')
    else:
        print('#' + str(k) + ' NO')