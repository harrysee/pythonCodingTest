# 모든 노드에서 다른 모든 노드까지의 최단경로 모두 계산
# 단계별로 거쳐가는 노드를 기준으로 알고리즘 수행
# 방문하지않은 노드 중 최단거리 갖는 노드 안찾아도됨
# 다이나믹 프로그래밍 유형에 속함
# 각단계마다 특정한 노드 k를 거쳐 가는 경우를 확인
    # a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사함
# 점화식 : D(ab) = min(D(ab), D(ak)+D(kb))
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] =0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY",end=' ')
        else:
            print(graph[a][b])