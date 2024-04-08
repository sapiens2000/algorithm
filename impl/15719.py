import sys

n = int(input())
sumN = sum(range(1, int(n)))
nums = sys.stdin.readline()
sumNum = 0
temp = ""

for num in nums:
    if num.isdigit():
        temp += num
    else:
        sumNum += int(temp)
        temp = ""

print(sumNum - sumN)