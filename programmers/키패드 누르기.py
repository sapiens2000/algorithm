def dist(target, pos):
    return abs(target[0] - pos[0]) + abs(target[1] - pos[1])


def solution(numbers, hand):
    pattern = {'L': (1, 4, 7), 'R': (3, 6, 9)}
    pos = {'L': [0, 3], 'R': [2, 3]}
    result = []

    def press(hand, coord):
        result.append(hand)
        pos[hand] = coord

    for num in numbers:
        choose = 'L'
        target = [0, (num - 1) // 3]

        if num in pattern['L']:
            pass
        elif num in pattern['R']:
            choose = 'R'
        else:
            target = [1, 3 if num == 0 else (num - 1) // 3]
            left, right = dist(target, pos['L']), dist(target, pos['R'])

            if right < left:
                choose = 'R'
            elif right == left and hand == 'right':
                choose = 'R'

        press(choose, target)

    return ''.join(result)