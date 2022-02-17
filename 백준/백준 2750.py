# N개의 수가 주어졌을때, 이를 오름차순으로 정렬하기

import sys

# 퀵정렬 구현
def quick_sort(array,start,end):
    if start >= end: return
    pivot = start   # 피봇 첫번째요소 설정
    left, right = start+1, end  # left위치 피봇바로 다음부터
    while left <= right:
        # 피봇보다 큰 데이터 찾기
        while left <= end and array[left] <= array[pivot]: left+=1
        # 피봇보다 작은 데이터 찾기
        while right > start and array[right]>=array[pivot]: right-=1
        # left,right 교차 시 작은데이터랑 피봇바꿔주기
        if left >= right:
            array[right], array[pivot] = array[pivot],array[right]
        else:   # 교차아니면 큰수,작은수 위치바꾸기
            array[right], array[left] = array[left],array[right]
    # 분할이후 정렬된 피봇을 제외한 나머지 부분에서 다시 정렬수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

t = int(input())
sortnum = list()
for i in range(t):
    sortnum.append(int(sys.stdin.readline()))

quick_sort(sortnum,0,len(sortnum)-1)
for s in sortnum:
    print(s)