arr = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while True:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(" ".join(map(str, arr)))

    if arr == answer:
        break