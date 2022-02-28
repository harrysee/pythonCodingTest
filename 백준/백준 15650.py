# N과 M (2)
# 1~N까지 중 중복없이 M개 고른 수열
# 고른 수열 오름차순 정렬 후 출력

# 이번 문제는 순서X, 중복X 조합임
# combination을 사용할 것이다.

from itertools import combinations

N,M = map(int,input().split())
for n in combinations(range(1,N+1),M):
    for i in n:
        print(i,end=' ')
    print()

# 중복없는 조합이였기에 combinations를 사용함
# 파이썬 옵션에서는 오름차순으로 정렬해서 제너레이션으로 전달해준다.