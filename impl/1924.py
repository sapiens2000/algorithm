a = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

m, d = map(int, input().split())

tmp = 0
for i in range(0, m-1):
    tmp += b[i]
tmp = (tmp+d) % 7

print(a[tmp])
