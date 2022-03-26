# 파이썬 정렬 라이브러리
# 1. sorted : 집합자료형, 딕셔너리 자료형 -> 정렬된 리스트자료형 반환(비파괴적 처리)
# 2. sort  : 리스트만 가능 -> 직접적으로 값을 바꿈(파괴적 처리)
# 3. 정렬 속성
    # a. sorted/sort에 key로 정렬기준 주기 : key=lamda x -> x[0]
    # b. reversed =True : 내림차순

array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

array.sort()
print(array)

arr = [('바나나',2),('사과',5),('당근',3)]
def setting(data):
    return data[1]

result = sorted(arr,key=setting)    # setting으로 값을 한개씩 넘겨서 반환된 값으로 정렬
print(result)

# 정렬 선택 방법 절리
    # 1. 정렬 라이브러리로 풀수 있는 문제 : 단순 정렬 기법은 물어보는 문제
    # 2. 정렬 알고리즘의 원리에 대해서 물어보는 문제 : 선택,삽입,퀵 정렬 등의 원리를 알고있어야 풀 수 있음
    # 3. 더 빠른 정렬이 필요한 문제 : 퀵 정렬 기반의 정렬 기법으로 안될 때, 계수 등 다른 정렬을 이용, 기존에 알려진 알고리즘의 구조적인 개선 거쳐야됨
