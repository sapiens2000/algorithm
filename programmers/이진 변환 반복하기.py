def solution(s):
    count = 0
    zeros = 0

    while s != '1':
        num = s.count('1')

        zeros += len(s) - num
        s = bin(num)[2:]
        count += 1

    return [count, zeros]