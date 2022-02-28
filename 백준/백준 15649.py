# N과 M (1)
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 파이썬 수열 옵션 사용하기
# itertools

from itertools import permutations

N,M = map(int, input().split())
for i in permutations(range(1,N+1),M):
    for n in i:
        print(n,end=' ')
    print()

# 중복없이 M개의 숫자를 고르는 순열옵션을 사용하여 해결하였다
# 초반엔 i만 출력해서 M개만큼 뽑는 개수가 달라질때 대응할수없엇다
# 이중 for문을 이용해서 동적으로 출력하게바꿈
# 중복없는 순열 이용 : permutations
# 중복순열 : product
# 조합 : combinations
# 중복조합 : combinations_with_replacement