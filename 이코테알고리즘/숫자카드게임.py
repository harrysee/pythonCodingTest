# 그리디
# 숫자가 쓰인 카드 N*M 형태
# 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
# 조건 ) 게임 룰 지켜야함 다음과 같음
    # N = 행의개수 / M= 열의개수
    # 뽑고자 하는 카드가 포함되어 있는 행 선택
    # 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드
    # 따라서 처음에 카드를 골라낼 행을 선택할 때, 가장 높은 숫자의 카드를 뽑을 수 있도록 전략

# 풀이 계획
# 입력 받기
# 이차원배열 정렬
# 가장 첫번째꺼에서 가장 작은 거 뽑기
import sys

N, M = map(int, input().split())
nums = list()
for i in range(N):
    nlist = list(map(int, sys.stdin.readline().split()))
    nums.append(min(nlist))

print(max(nums))

# 줄마다 가장 작은 것들만 배열에 추가하여 그 중 가장 큰 수를 출력함

