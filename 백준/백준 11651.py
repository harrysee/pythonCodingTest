# 좌표 정렬하기 2
# 파이썬에서 다차원배열을 정렬하는 옵션을 제공하여 그것을 사용하기로함
# 람다 함수로 정렬기준에 1인덱스로 1차정렬,0으로 2차정렬을하였다.

import sys
t = int(input())
nums = list()
for i in range(t):
    nums.append(list(map(int,sys.stdin.readline().split())))
nums.sort(key=lambda x:(x[1],x[0]))

for n in nums:
    print(n[0],n[1])