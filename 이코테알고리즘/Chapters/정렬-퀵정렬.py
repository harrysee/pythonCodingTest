# 퀵정렬 : 기준데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸자
# 가장 많이 사용됨, 병합정렬도 퀵만큼 빠름
# pivot : 큰숫자와 작은 숫자를 교환 할 때 기준이 되는 값 / pivot을 설정하고 리스트를 분할하는 방법에 따라 퀵정렬을 구분
# 호어 분할 : 대표적인 분할 방식 -> 리스트에서 첫 번째 데이터를 피벗으로 정한다.
# 1. 피벗을 첫번째 데이터로 설정
# 2. left,rigth 각각 피벗보다 큰 값, 피벗보다 작은 값을 찾는다
# 3. 각자 값을 찾아서 큰값과 작은값을 스위치시킨다
# 4. left,rigth가 엇갈리면 right에 피벗을 넣는다(어차피 엇갈리기 전까지의 데이터들에 이제 피벗보다 큰값은 없기때문)
# 5. pivot은 정렬이 된거임 > 피벗을 중심으로 왼쪽그룹, 오른쪽그룹 각각 위의 정렬방식대로 동작한다.
# 6. 각 원소가 한개씩 남으면 정렬완료
# 시간복잡도 : 평균시간복잡도는 O(N log N) / 데이터가 이미 정렬되어 있는 경우 : O(N^2) -최악의 경우

array = [5,7,9,0,3,1,6,2,4,8]

# 전통 퀵 정렬 분할 방식 : 널리 사용되는 가장 직관적인 형태
def quick_sort(array, start, end):
    if start>=end: # 원소가 한개인 경우 종료
        return 
    pivot = start
    left = start+1
    right = end
    while left<=right:  # 엇갈리기 전까지
        while left<=end and array[left]<=array[pivot]: left+=1 # 피벗보다 큰 값 인덱스 찾기
        while right>start and array[right]>=array[pivot]: right-=1 # 피벗보다 작은 값 인덱스 찾기
        if left>right: # 엇갈리면 피봇<->작은데이터
            array[pivot],array[right]=array[right],array[pivot]
        else:   # 안엇갈리면 각자 찾은거니까 큰데이터<->작은데이터 해주기
            array[left],array[right]=array[right],array[left]
        # 분할 이후 왼쪽 부분, 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)

# 파이썬의 장점으로 짧게 작성한 퀵정렬 : 시간 면에선 좀 더 비효율적이나 더 직관적
def quick_sort_python(array):
    # 리스트가 하나 이하의 원소만을 담고 있으면 종료
    if len(array)<=1:
        return array
    
    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x<=pivot]   # 분할된 왼쪽 부분 : 같거나 작은 값들만
    right_side = [x for x in tail if x>pivot]   # 분할된 오른쪽 부분 : 큰 값들만
    
    # 분할 이후 왼쪽 정렬과 오른쪽 부분 각각 정렬을 수행한 후, 전체리스트를 반환
    return quick_sort_python(left_side)+[pivot]+quick_sort_python(right_side)

        
quick_sort(array,0,len(array)-1)
quick_sort_python(array)
print(array)



