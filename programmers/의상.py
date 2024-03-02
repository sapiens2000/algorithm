def solution(clothes):
    d = {}
    answer = 1

    for tmp in clothes:
        name, type = tmp[0], tmp[1]

        if d.get(type):
            d[type] += 1
        else:
            d[type] = 1

    for k in d:
        answer *= (d[k] + 1)

    return answer - 1