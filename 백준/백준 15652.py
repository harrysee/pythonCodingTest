# N과 M (4)
# 1~N 중 M개 고른 수열
# 중복가능
# 비내림차순 = 걍 오름차순같음

# 중복조합이기 때문에 combination_with_replacement를 사용할 것
from itertools import combinations_with_replacement

N,M = map(int,input().split())
for n in combinations_with_replacement(range(1,N+1),M):
    for i in n:
        print(i,end=" ")
    print()