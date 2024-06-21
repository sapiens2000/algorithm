# def solution(s):
#     dct = {
#         "zero": "0",
#         "one": "1",
#         "two": "2",
#         "three": "3",
#         "four": "4",
#         "five": "5",
#         "six": "6",
#         "seven": "7",
#         "eight": "8",
#         "nine": "9",
#     }
#
#     for k, v in dct.items():
#         s = s.replace(k, v)
#
#     return(int(s))

def solution(s):
    translation = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    answer = ''
    tmp = []

    for c in s:
        if c.isdigit():
            if len(tmp) > 0:
                check = ''
                for d in tmp:
                    check += d
                    if check in translation:
                        answer += translation[''.join(check)]
                        check = ''
                tmp = []
            answer += c
        else:
            tmp.append(c)

    if len(tmp) > 0:
        check = ''
        for c in tmp:
            check += c
            if check in translation:
                answer += translation[''.join(check)]
                check = ''

    return int(answer)
