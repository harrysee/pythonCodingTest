# 보내고자하는 메시지 있는 경우 다른 도시로 전보 보내서 메시지 전송 가능
# X라는 도시 -> Y라는 도시로 전보 보낼려면 도시X에서 Y로 향하는 통로 설치되어있어야함
# 통로 없으면 메시지 못보냄
# 통로 거쳐서 보낼려면 일정시간 소요
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수, 모두 메시지 받는데까지 걸리는 시간 계산하기

# 입력
# 첫째줄 : 도시개수N, 통로개수M, 보내고자하는 도시C
#    (1 <= N <= 30,000, 1 <= M <= 200,000, 1 <= C <= N)
# 둘째줄~ : 통로에 대한 정보 X,Y,Z : 특정 도시 X에서 다른 특정 도시 Y로 Z시간만큼됨

# 출력
# 도시의 총 개수와 총 걸리는 시간 공백으로 구분하여 출력
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N,M,C = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for i in range(M):
    x,y,z = map(int,input().split())
    graph[x].append([y,z])

# 다익스트라 알고리즘
def getTimes(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

getTimes(C) # 시작 도시 맞춰주기
print(graph)
print(distance)
cnt = len(distance)-1 # 자기자신을 빼고 나머지 개수 카운트
times = -1
for d in distance:
    if d==INF:  # 닿지 않는 도시가 있으면 카운트-1을 한다
        cnt-=1
    elif times < d: # 닿는 거리중 가장 많이 걸리는 시간 구하기
        times=d

print(cnt,times)
