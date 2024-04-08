d = set(['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='])

arr = input().rstrip()
cur = 0
cnt = 0

while cur < len(arr):
    if arr[cur:cur+3] in d:
        cur += 3
    elif arr[cur:cur+2] in d:
        cur += 2
    else:
        cur += 1
    cnt+=1

print(cnt)
