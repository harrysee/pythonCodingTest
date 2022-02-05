# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다.
# 비어잇는 집 없음
# 모든 거주민들이 이계약조건 지킴
# 주어지는 양의 정수 k와 n에 대해 k층의 n호에는 몇명이 살고있는지 구하기
# 아파트 - 0층부터, 각층에는 1호부터 0층 i호에는 i명 거주

# 풀이 > 힌트를 좀 얻었다
# 현호실 사람수 = 한층밑현호실+1사람수
# 1층 2호사람수 = 0층 3호 사람수
# 1층 2호+ 0층 3호 = 1층 3호
import sys

t= int(input())

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    k0 = [i for i in range(n+1)]

    for _k in range(k):
        for _n in range(n+1):
            k0[_n] +=k0[_n-1]
    print(k0[-1])
    
# 한줄평 : 누적시킨다는것까진 알았는데 어떤식으로 누적을 시켜야할지 생각하지못하였다.ㅠ
# 누적을 시킬때 앞층 뒷층 경우를 다 생각해봐야겠다.
# https://ooyoung.tistory.com/89