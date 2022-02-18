# 통계학
# N개의 수를 대표하는 기본 통계값- N은 홀수
# 네가지 기본 통계값 구하기
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
import sys
# 입력받기
t = int(input())
nums = [0]*t
for i in range(t):
    nums[i]= int(sys.stdin.readline())

# 최빈값 : 딕셔너리의 각 키에 개수를 센다 -> 최빈값의 키만 모아서 리스트 만듬
result ={n:0 for n in nums}
for n in nums:
    result[n] +=1
value = [k for k,v in result.items() if max(result.values()) == v]

nums.sort()
print(round(sum(nums)/t))
print(nums[t//2])
# 최빈값이 여러개면 정렬해서 두번째로 작은값출력 / 아니면 걍 첫번째 출력
if len(value)>1:
    value.sort()
    print(value[1])
else:
    print(value[0])
print(nums[-1]-nums[0])
# 이 코드 딕셔너리로 삽질했는데 아직도 뭐가 문젠지 모르겠다. 자꾸 틀렸다함;
# 21퍼센트를 넘지못햇다..왤카
# 헐 round 때문이였다. 최빈값..나의 코드가 틀린줄알고 짖짜..;;;
# round가 아니라 값 첫번째 나누기 할때 sum(nums)//t로 했더니만 걍 잘려서그랬다.


# Counter을 사용한 코드도 빠르고 좋아서 적어본다.
import sys
from collections import Counter
n = int(sys.stdin.readline())
m = [int(sys.stdin.readline()) for _ in range(n)]

# 산술 평균
print(round(sum(m) / n))

# 중앙 값
m.sort()
print(m[n//2])

# 최빈값
cnt = Counter(m).most_common(2) # 가장 개수가 많은 k개의 데이터를 리턴

# 데이터가 2개 이상일 경우
if len(cnt) > 1:
    # 2개의 데이터의 value 값이 같은지 확인
    # 같다면 두 번째 key 값을 출력
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])

    # 다르다면 첫 번째 key 값을 출력
    else:
        print(cnt[0][0])

# 데이터가 하나라면 첫 번째 key 값을 출력
else:
    print(cnt[0][0])

# 범위
print(max(m) - min(m))

