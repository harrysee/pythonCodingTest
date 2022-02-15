# 블랙잭
# 브루트포스 알고리즘 이용
# 브루트 포스 알고리즘 : 검색 대상이 되는 원본 문자열의 처음부터 끝까지 차례대로 순회하며 
# 문자들을 일일이 비교하는 방식의 고지식한 알고리즘
# 비교하고자 하는 문자열과패턴을 한칸씩 이동하며 일치여부 확인

# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
# 모든 카드에는 양의 정수
# 제한된 사간안에 N장의 카드 중에서 3장의 카드를 골라야한다.
# M을 넘지않으면서 M과 최대한 가깝게

# 계획
# N,M 입력받기
# 배열 cards
# 인덱스로 생각
# 1. 일단 정렬
# 2. 3개이기때문에 threesum
# for문 - 인덱스 차례대로 순회
# max 변수 -가장 가까운값 담을거임
#   while True
        # 인덱스 i = for c+1
        # 인덱스 j = -1 (맨끝)
        # if M>= c+i+j >max:
            # break
        # elif c+i+j>M:
            # j-=1
        #else:
            # i+=1
# max출력

# 코드 --------------------------------------------------
import sys
N,M = map(int, sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
max = -1
cards.sort()
for x,c in enumerate(cards):
    i = x + 1
    j = len(cards)-1
    while i<j:
        rest =c+cards[i]+cards[j]
        if M>=rest>max:
            max = rest
        elif rest>M:
            j-=1
        else:
            i+=1
print(max)

# 1. 조건문 브레이크 
#         if M>=rest>max:
#             max = rest
# 이부분에서 브레이크를 걸었다가 버그가 났다. 이유는 여기서 나왔다고 막아버리면 그 뒤에
# 더 있을수도 있기때문이다. -> 어차피 i<j로 계산하여 끝에 도달하면 멈춤
# 2. 72ms걸림 -> for문의 원포인트와 안에서 투포인트를 사용하여 두번의 반복문을 사용하였다.
# 3. j를 처음에 -1부터 --1씩 감소시키며 i>j로 주니 끝나지않아서 당황했다..
# 인덱스를 주의하여 계산한 풀이였다. -나혼자품~~