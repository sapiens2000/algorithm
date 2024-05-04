n = int(input())
arr = [i for i in range(1, n+1)]
result = []
idx = 0

while len(arr) != 1:
    result.append(arr.pop(0))
    arr.append(arr.pop(0))

for num in result:
    print(num,end=' ')
print(arr[0])