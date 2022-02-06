# 소수찾기
# 주어진 수 N개 중에서 소수가 몇개인지 찾아서 출력
N = int(input())
nums = list(map(int, input().split()))
isSosu = len(nums)-nums.count(1)
for n in nums:
    for i in range(2,n):
        if n%i==0:
            isSosu-=1
            break
print(isSosu)

# 한줄평
# 이전에도 소수 구하는 문제는 많이 풀어봐서 쉬웠다.
# 코드를 짤때 1을 생각하지않고 짜서 헷갈린 점이 있었다.