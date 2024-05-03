from collections import deque


n = int(input())
arr = deque([i for i in range(1, n+1)])
result = []
idx = 0

while True:
    if len(arr) == 1:
        break
    head = arr.popleft()
    result.append(head)
    arr.append(arr.popleft())


for num in result:
    print(num,end=' ')
print(arr[0])