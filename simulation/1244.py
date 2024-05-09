n = int(input())
switches = list(map(int, input().split()))

students = int(input())

for _ in range(students):
    sex, num = map(int, input().split())

    if sex:
        for i in range(1, n+1):
            if i%num == 0:
                switches[i-1] =
    else:



for s in switches:
    print(s, end=' ')