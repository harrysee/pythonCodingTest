# dfs
# 매개변수 그래프, 현위치, 방문기록
# 현재 방문처리
# 출력
# 폴문 그래프 현재 연결된 노드들 가져오기
    # 방문하지않았다면
        # 재귀호출로 들어가기

def dfs(graph, v, visited):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
# 음료수 얼려먹기
# x,y 위치 가져오기
# 주어진 범위 체크
# 0이면 x,y 를 칸막이로 바꾸고 그래프에서 상하좌우 호출

N, M = map(int,input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

def ice(x,y):
    if x>N-1 or x<0 or y>M-1 or y<0:
        return False

    if graph[x][y]==0:
        graph[x][y] = 1

        ice(x+1,y)
        ice(x-1,y)
        ice(x,y-1)
        ice(x,y+1)
        return True
    return False

result =0
for i in graph:
    for j in i:
        if ice(i,j):
            result+=1





























