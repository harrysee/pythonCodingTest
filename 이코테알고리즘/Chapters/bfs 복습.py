# bfs 알고리즘
# 함수 매개변수 : graph, start, visited
    # 큐 생성 : deque
    # start 방문처리
    # 큐 있을동안 와일
        # 큐에서 한개 빼기
        
        # 그래프에서 반복
            # 방문안되어있으면
                # 큐에 넣기
from collections import deque


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[now]:
                q.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5]
]

visited = [False]*4
bfs(graph,1,visited)