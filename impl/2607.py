# 길이가 같은경우
# 길이가 긴 경우
# 길이가 작은 경우

# set 으로 할 경우 문자 구성이 같은 단어 카운트 X
n = int(input())
result = 0
first = list(input())


for _ in range(n-1):
    word = list(input())

    if abs(len(word)-len(first)) >= 2:
        continue
    else:
        tmp = first[:]
        cnt = 0

        for c in word:
            if c in tmp:
                tmp.remove(c)
            else:
                cnt += 1

        if len(tmp) < 2 and cnt < 2:
            result += 1

print(result)
