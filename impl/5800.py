k = int(input())
for i in range(k):
    arr = list(map(int, input().split()))
    arr = sorted(arr[1:], reverse=True)


    form1 = f'Class {i+1}'
    gap = 0
    for j in range(1, len(arr)):
        if (arr[j-1] - arr[j]) > gap:
            gap = arr[j-1] - arr[j]

    form2 = f'Max {arr[0]}, Min {arr[-1]}, Largest gap {gap}'
    print(form1)
    print(form2)
