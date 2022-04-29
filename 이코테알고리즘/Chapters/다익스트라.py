# 다익스트라 알고리즘
# 그래프에서 여러개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단경로 구함
# 음의 간선이 없을 때 정상적으로 동작
# 1. 출발노드 설정
# 2. 최단 거리 테이블 초기화하여 처음 세팅
# 3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산하여 최단거리 테이블 생성
# 5. 위 과정에서 3,4번 반복
# ----------------
# 구현 방법
# 구현 쉽지만 느리게 동작 / 구현 까다롭지만 빠르게 동작
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값 =10억으로 설정

# 노드의 개수, 간선의 개수
n,m = map(int,input().split())
#시작노드
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)   # 방문했는지 체크하는 리스트
distance = [INF] * (n+1)    # 최단거리 테이블 무한으로 초기화

for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b로 가는 비용(거리)가 c라는 의미
    graph[a].append([b,c])

# 최단 거리 가장 짧은 노드 위치 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        # 최단 거리여야하고, 방문하지 않았어야함
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] =0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1 노드에 대해 반복
    for i in range(n-1):
        # 최단 거리가 가장 짧은 노드 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우 무한으로 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

