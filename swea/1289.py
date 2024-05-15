t = int(input())

for case in range(1, t+1):
    bits = input()
    init = list('0' * len(bits))
    result = 0

    for i in range(len(bits)):
        if init[i] != bits[i]:
            for j in range(i, len(bits)):
                init[j] = bits[i]
            result += 1

        if init == bits:
            break

    print(f'#{case} {result}')