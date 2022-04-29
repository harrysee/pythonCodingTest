# 개선된 다익스트라
# 힙 구조 사용
    # 힙 : 바이너리 트리로 구현됨
    # 우선순위로 빠져나오는 자료구조 - heapq 사용(minHeap, maxHeap)
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())    # 시작노드
# 원래 노드의 정보를 담는 리스트 
graph = [[] for i in range(n+1)]
# 최단거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append([b,c])
    
def dijkstra(start):
    q =[]
    # 첫 시작노드 세팅 : 최단경로 0으로 설정해 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        # 최단 거리가 가장 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist+i[1]
            # 현재 노드 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 외우기
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split()) # 노드개수, 간선개수
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])

def dijastra(start):
    q = []
    distance[start] =0
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] <dist:
            continue

        for i in graph[now]:
            cost = dist+ i[1]

            if cost< distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijastra(start)

for i in range(n):
    if distance[i]== INF:
        print("거리가 닻지않음")
    else:
        print(distance[i])












