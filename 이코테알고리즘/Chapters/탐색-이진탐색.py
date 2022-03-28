# 이진 탐색 : 반으로 쪼개면서 탐색하는 기법
# 배열내부의 데이터가 정렬되어 있어야만 사용 가능 - 무작위 불가능
# 탐색 범위를 절반씩 좁혀가며 데이터 탐색 : 찾으려는 데이터와 중간점위치의 데이터를 반복비교
# 1. 변수 세개 준비 : 범위 시작점/ 끝점 / 중간점
# 2. 중간점 데이터와 찾으려는 데이터 비교
    # a. 중간점데이터가 더 크면 끝점을 중간점-1로 옮김
    # b. 중간점 데이터가 더 작으면 시작점을 중간점+1로 옮김
    # c. 중간점과 데이터가 같으면 종료한다.
# 3. 시작점과 끝점이 같거나 엇갈리면 종료하고 데이터없음
# O(logN) : 절반씩 줄어들도록 만듬
# 구현방법 : 재귀함수 / 반복문 이용

# 1. 재귀함수로 구현
def binary_search(array,target,start, end): # 배열,찾을값, 시작, 끝
    if start>end:
        return None
    mid = (start+end)//2    # 중간 인덱스
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        binary_search(array,target,start,mid-1)
    else:
        binary_search(array,target,mid+1,end)

# 2. 반복문으로 구현
def binary_search_while(array,target,start,end):
    mid = (start+end)//2
    while start <=end:  # 원소가 있을동안만
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end -= 1
        else:
            start+=1
    return None

n,target = list(map(int, input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result==None:
    print("존재안함")
else:
    print(result,"에 존재함")


    