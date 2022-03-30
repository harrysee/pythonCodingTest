# 전자매자의 부품 N개는 정수형태의 고유한 번호가 있다.
# 손님이 M개 종류의 부품을 대량으로 구매하겠다했으므로 격적서 작성해야함
# -> 가게 안의 부품이 모두 있는지 확인하기

# 탐색 방법을 통해 해당 부품들을 검색해야한다. : 이진탐색 이용
import sys

def search(arr,target,start, end):
    if start> end:
        return False
    mid = (start+end)//2
    if arr[mid]== target:
        return True
    elif arr[mid]>target:
        return search(arr,target,start,mid-1)
    else:
        return search(arr,target,mid+1,end)

N = int(input())
items = list(map(int, sys.stdin.readline().split()))
M = int(input())
searchs = list(map(int, sys.stdin.readline().split()))
items.sort()


for s in searchs:
    if search(items,s,0,N-1):
        print('yes',end=' ')
    else:
        print('no',end=' ')


# 이진 탐색 재귀문을 쓸때는 start>end 조건과 재귀호출에 return을 붙여줘야한다 명심!