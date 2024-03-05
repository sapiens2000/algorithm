def solution(prices):
    answer = [0] * len(prices)
    s = []

    for i in range(len(prices)):
        while s and prices[i] < prices[s[-1]]:
            past = s.pop()
            answer[past] = i - past
        s.append(i)

    for i in s:
        answer[i] = len(prices) - 1 - i

    return answer