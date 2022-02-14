# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

import sys
dots = list(map(int, sys.stdin.readline().split()))
result = ""

if dots[0]==dots[1]==dots[2]:
    result=10000+dots[0]*1000
elif dots[0]!=dots[1]!=dots[2]!=dots[0]:
    result=(100*max(dots))
else:
    result = 1000+dots[0]*100 if dots[0]==dots[1] or dots[0]==dots[2] else 1000+dots[1]*100
print(result)

# 3 3 4, 3 4 4 이런것만하고  6 2 6 이런 테스트는 두번째에서 걸리는 바람에
# dots[0]!=dots[1]!=dots[2]!=dots[0] 이 조건을 넣고
# 마지막 조건문 or도 추가했다...비효율적일수있지만 if문을 왕창써서 통과했다.