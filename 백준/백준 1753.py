# 최단경로
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램
# 조건 : 모든 간선 가중치 = 10이하 자연수 / V,E 둘다 1부터 시작
# 입력
# 1. 정점개수V, 간선개수E
# 2. 시작 정점 번호 K
# 3~E개 : u,v,w = u에서 v로 가는 가중치 w인 간선
# 출력
# 첫째 줄부터 V개의 줄에 걸쳐 i번째 줄에 i 정점으로의 최단 경로 경로값 출력, 
# 경로 존재 안하면 INF 출력
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

V,E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
