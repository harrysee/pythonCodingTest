# 선택 정렬
# 동작 : 남은 범위에서 가장 작은 수 찾기, 작은수와 남은범위 첫번째 요소와 스위치
# 탐색범위는 반복할 때마다 줄어듬. 매번 가장 작은 원소를 찾기 위해서
# 탐색범위만큼 데이터를 확인, 매번 선형탐색을 하는 것과 동일
    # 선형 : 그냥 처음부터 끝까지 계속 돌아다니면서 정렬
# 시간복잡도 : N번만큼 작은 수를 찾아서 맨앞으로 보냄
    # -> N + (N-1)+ (N-2) + ....+ 2
    # (N^2+N-2)/2 -> 빅오표기법 : O(N^2)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index]> array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index],array[i]

print(array)