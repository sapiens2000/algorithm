n = int(input())
tmp = n

cycle = 0

while True:
    if tmp < 10:
        tmp = '0' + str(tmp)

    arr = str(tmp)
    first, second = arr[0], arr[1]
    tmp = int(second + str(int(second) + int(first))[-1])

    cycle += 1

    if tmp == n:
        break

print(cycle)