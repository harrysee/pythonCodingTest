'''
5.빈 리스트에서 기존의 값들보다 큰 값이 추가될 때마다 카운팅
ex) 빈 리스트에서 [1, 3, 2, 6, 4, 9, 5]가 추가되는 상황
'''

emptylist = []
nums = [1, 3, 2, 6, 4, 9, 5]
cnt =0

for n in range(nums):
    for e in range(emptylist):
        if n > e :
            cnt+=1
            break