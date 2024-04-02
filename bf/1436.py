n = int(input())
num = 666
idx = 0

while True:
    if '666' in str(num):
        idx += 1

    if idx == n:
        print(num)
        break

    num += 1