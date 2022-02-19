# 소트 인사이드
# 수가 주어지면 그수의 각 자리수를 내림차순으로 정렬
# ex) 2148 -> 8421
N = input()
nums = list(map(int,N))
for n in sorted(nums,reverse=True):
    print(n,end='')

# 수를 문자열로 받아서 각각 int형으로 변환 후 정렬하였다. 
# 조인을 쓸까 하였지만 배열은 합쳐지지않아 그냥 for문으로 순서대로 출력함