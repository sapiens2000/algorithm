def solution(word):
    answer = 0
    data = []
    dfs(data, '', 0)

    for i in range(len(data)):
        if data[i] == word:
            answer = i + 1
            break

    return answer


def dfs(data, p, idx):
    if idx == 6:
        return

    if p != '': data.append(p)

    for c in ('A', 'E', 'I', 'O', 'U'):
        dfs(data, ''.join([p, c]), idx + 1)