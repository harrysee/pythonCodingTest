# 미래도시-다익스트라
# 판매원 A는 미래도시에있음
# 1번부터 N번까지 회사있고, 특정회사끼리는 서로 도로를 통해 연결됨
# 1번회사에 위치해 있고, X번회사에 방문해 물건 판매
# 그러나 소개팅 참여해야되기 때문에 K회사를 반드시 들러야한다.
# -> K회사를 들러서 X회사로 갈때 가장 빨리 가는 경로 구하기

# 첫째 줄 : 회사개수N, 경로개수M 공백으로 구분
# 둘째 줄~M+1 :  연결된 두 회사의 번호 공백으로 주어짐
# M+2 : X,K 공백으로 구분되어 주어짐
# 도달x : -1 출력
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
# 그래프 세팅
graph = [[INF]*(n+1) for _ in range(n+1)]
for a in range(n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b]=0

# 연결된 회사들 입력받기
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = 1
X,K = map(int,input().split())

# 그래프 최단경로 구하기
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

start = 1 # 현재 A의 위치
distance = graph[start][K]+graph[K][X]
if distance==INF:
    print(-1)
else:
    print(distance)

# for문 3개를 꼭 써줘야하는 이유는 모두 연결되어있기때문에
# 다 돌아가면서 최적화 시켜줘야한다.