# 5.빈 리스트에서 기존의 값들보다 큰 값이 추가될 때마다 카운팅
# ex) 빈 리스트에서 [1, 3, 2, 6, 4, 9, 5]가 추가되는 상황
def counting(nums):
    cnt=0
    max =-1
    for n in nums:
        if n>max:
            max = n
            cnt += 1
    return cnt

print(counting([1, 3, 2, 6, 4, 9, 5]))

# 풀이 1 -
arr = [1, 3, 2, 6, 4, 9, 5]
count =0
max =-1     # 범위 신경쓰기 **
for x in arr:
    # x 값과 max값보다 크다면
    if x>max:
        # max값을 x로 갱신
        max = x
        count+=1

# 풀이 2 -
arr = [1, 3, 2, 6, 4, 9, 5]
count =0
max = arr[0]
for x in arr[1:]:
    # x 값과 max값보다 크다면
    if x>max:
        # max값을 x로 갱신
        max = x
        count+=1

