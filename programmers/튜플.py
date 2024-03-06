def solution(s):
    answer = {}
    s = s[2:-2].split("},{")

    s = sorted(s, key=lambda x: len(x))

    for item in s:
        item = list(map(int, item.split(",")))
        for value in item:
            if value not in answer:
                answer[value] = 1

    return list(answer)