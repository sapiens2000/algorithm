def solution(participant, completion):
    cnt = {}

    for p in participant:
        if p in cnt:
            cnt[p] += 1
        else:
            cnt[p] = 1

    for c in completion:
        cnt[c] -= 1

    for k in cnt:
        if cnt[k] >= 1:
            return k

    return ''