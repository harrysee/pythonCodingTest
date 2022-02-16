# 덩치
# 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수 계산
# 예를 들어 어떤 A, B 두 사람의 덩치가 각각 (56, 177), (45, 165) 라고 한다면 A의 덩치가 B보다 큰 셈
# 키와 몸무게가 다크면 당연히 더 큰사람이 큰사람임
# 그런데 서로 다른 덩치끼리 크기를 정할 수 없는 경우
# -> 예를 들어 두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면 몸무게는 D가 C보다 더 무겁고,
# 키는 C가 더 크므로, "덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다.

# 계획 코드
# 입력 개수, 배열
# 변수 등수를 담을 배열
# for문 순서대로
    # for문 자신제외
        # width,hight가 자기가더작으면 +=1
# 등수출력 for문

import sys
N = int(input())
infos = list()
ranks = [1]*N
for i in range(N):
    infos.append(list(map(int,sys.stdin.readline().split())))

for k,info in enumerate(infos):
    for ifo in infos:
        if info==ifo: continue
        if ifo[0]>info[0] and ifo[1]>info[1]:
            ranks[k]+=1

for r in ranks:
    print(r,end=" ")


# 한번에 맞게 잘풀었다
# 설명하자면 처음에 자기보다 더 큰게있으면 원래등수에서 -1을 할려고했지만 그러면
# kg은 큰데 키가 작은경우에는 -1이 안되기에 for문을 돌면서 자기가 작으면 등수를 한개씩 내리는+1을하였다
# 이중for문을 이용하여 다소 효율적이진않을수있지만 키,몸무게를 따로 비교하지않아서 좋은코드라고 생각
# 키랑 몸무게가 다르면 등수가 같은것은 사실 함정이였던걸수도