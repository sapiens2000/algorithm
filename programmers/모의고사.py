def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    answer = []

    for i in range(len(answers)):
        if first[i % 5] == answers[i]:
            score[0] += 1
        if second[i % 8] == answers[i]:
            score[1] += 1
        if third[i % 10] == answers[i]:
            score[2] += 1

    m = max(score)
    for idx, s in enumerate(score):
        if s == m:
            answer.append(idx + 1)

    return answer