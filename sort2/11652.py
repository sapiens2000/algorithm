n = int(input())
dict = {}

for _ in range(n):
    key = int(input())
    if dict.get(key):
        dict[key] += 1
    else:
        dict[key] = 1

result = max(dict.values())

for key in sorted(dict.keys()):
    if dict[key] == result:
        print(key)
        break
