# 네트워크란 컴퓨터 상호 간에 정보를 교환 할 수 있도록 연결된 형태
# A와 B 컴퓨터가 직접적으로 연결되어있고, B와 C가 직접적으로 연결되어있을 경우 ABC는 모두 같은 네트워크 상에 있다.
# 컴퓨터 개수 n, 연결에 대한 정보 2차원 배열 computers가 매개변수 : 네트워크의 개수는?

# 컴퓨터의 개수 n은 1이상 200 이하의 자연수
# 각 컴퓨터는 0부터 n-1인 정수
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1이다.

# 아이디어
# dfs로 모든 루트를 방문하며 자기자신이 아닌 방문한 곳이 있으면 그곳으로 이동하면서 짠다.

n =0
computers = []
visited = []
def solution(n1, computers1):
    global n,computers,visited  # 개수, 배열, 방문기록
    n, computers = n1, computers1
    visited = [False]*n # 방문기록
    cnt =0      # 카운트
    for i in range(n):  
        if not visited[i] and network(i):   # 방문하지않았으면 함수실행해서 카운트
            cnt+=1
    return cnt

def network(v):
    visited[v] = True   # 방문 처리
    # 인접 행렬 풀이
    for w in range(n):  # 배열 개수만큼 for문
        if computers[v][w] and not visited[w]:  # 연결되고 방문되지 않았다면
            network(w)  # 이동
    # 인접 리스트 풀이
    # for w in graph[v]:  # 배열 개수만큼 for문
    #     if not visited[w]:  # 연결되고 방문되지 않았다면
    #         network(w)  # 이동
    # 핵심문장 복습
    # for w in range(n):
    #     if computers[v][w] and not visited[w]:
    #         network(v)
    return True

print('결과',solution(3, [[1,1,0],[1,1,0],[0,0,1]]))
print('결과',solution(3, [[1,1,0],[1,1,1],[0,1,1]]))

# dfs 행렬을 사용하는 방법을 익혔다 굳~
# dfs의 핵심은 visited이다 
# 행렬이나 인접이나 무조건 명심하자


