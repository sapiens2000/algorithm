n = int(input())
first = list(input())
length = len(first)

for i in range(n - 1):
    other = list(input())

    for j in range(length):
        if first[j] != other[j]:
            first[j] = '?'

print(''.join(first))