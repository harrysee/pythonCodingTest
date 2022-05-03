# 특정거리의 도시 찾기 : BFS/DFS
# p339
# 도시 1~N번까지, M개의 단방향 도로가 존재 / 모든 도로의 거리는 1
# 특정한 도시 X로 출발하여 도달가능한 모든 도시에서 최단거리가 정확히 K인 모든 도시의 번호를 출력하기
# 입력
# 도시개수N, 도로개수M, 거리정보K, 출발도시X
# 둘째 줄부터 M개의 줄에 걸쳐 두개의 자연수 A,B : 각 자연수는 공백 구분
    # A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는의미
# 출력
# 한줄에 하나씩 오름차순
# 존재안하면 -1 출력
import sys
from collections import deque

input = sys.stdin.readline
n,m,k,x = map(int, input().split())
citys = [[] for _ in range(n+1)]
dict = [0]*(m+1)    # 최단경로를 담을 배열 생성
for i in range(m):
    A,B = map(int,input().split())
    citys[A].append(B)

def load(start):
    q = deque([start])

    while q:
        now = q.popleft()
        for c in citys[now]:
            if dict[c]==0:  # 방문 안한 곳이면
                q.append(c) # 큐에 담기
                dict[c] = dict[now]+1   # 이전 경로길+1로 현재경로 처리하기

load(x)
keys = []   # 경로가 k인것만 담기
for i,d in enumerate(dict):
    if d==k:
        keys.append(i)
if len(keys)==0:    # 한개도 없으면 -1 리턴
    print(-1)

for k in sorted(keys):  # 오름차순
    print(k)

# bfs 알고리즘을 응용해서 경로 배열을 추가하였다
# 스스로 해결하여 뿌듯하다.