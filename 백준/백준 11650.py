# 좌표정렬하기
# 2차원평면 위에 점 N개가 주어짐
# 좌표 x 오름차순 정렬, x좌표가 같으면 y오름차순 2차정렬

# 파이썬 기본제공 sort는 이차원배열 정렬시 기본값으로
# 첫번째 인덱스로 정렬, 같은값일시 두번째오름차순으로 재정렬 시켜줌
import sys
t = int(input())
nums=list()
for i in range(t):
    nums.append(list(map(int,sys.stdin.readline().split())))
nums.sort()
for n in nums:
    print(n[0],n[1])

# 파이썬의 기본함수 sort를 이용해서 쉽게 정렬했다.
# 이차원 배열 기본정렬 옵션을 배웠다.