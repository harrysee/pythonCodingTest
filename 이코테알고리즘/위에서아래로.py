# 정렬 : 위에서 아래로 p178
# 입력된 수열을 내림차순으로 정렬하여라
# 조건) 수의 범위는 1이상 100,000 이하이다 -> 100,000이하이므로 라이브러리 이용

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort(reverse=True)
for n in nums:
    print(n,end=' ')
    