# DFS/BFS
# 식초는 NxM 크기의 직사각형 형태의 미로에 갇힘,
# 여러마리 괴물 피해 탈출해라
# 식초 위치(1,1) / 미로 출구(N,M) : 한번에 한 칸씩 이동 가능
# 괴물 있는 부분은 0, 괴물 없는 부분은 1, 미로는 반드시 탈출 ㄱㄴ한 형태
# 식초가 탈출하기 위해 움직여야하는 최소 칸의 개수 : 시작칸&막칸 포함

# 풀이계획
# 입력 : N,M (세로,가로) :공백X 붙어서, 시작칸막칸은 1
# BFS 이용 : 가까운 노드부터 모든 노드 탐색
# 상하좌우로 연결되는 모든 노드 거리 1로 동일함
# 매번 새로운 지점 방문 시 이전지점까지 거리 +1 기록
# => 갈 수있는 곳을 탐색하며 해당 배열에 최단거리를 저장, 도착지점의 최단거리 기록
import sys
from collections import deque

def bfs_road(x,y):
    global maze
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx, ny =x+dx[i],y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if maze[nx][ny]==1:
                queue.append((nx,ny))
                maze[nx][ny] = maze[x][y]+1

N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline()[:-1])))

bfs_road(0,0)
print(maze[N-1][M-1])

# 코드 이해한대로 설명하기
# 1. 입력받아서 함수 호출
# 2. BFS이기에 재귀호출은 하지않음
# 3. 큐 세팅, 동서남북 커서 세팅, 큐에 초기값 넣음
# 4. while문 queue에 값이 있을 경우에만 반복함(queue는 마지막까지 값을 꺼내서 비교)
# 5. x,y 변수에 queue 값 중 제일 먼저 넣은 값을 가져옴
# 6. 동서남북 반복문 돌림
# 7. 가져온 현재 노드를 기준(x,y)으로 동서남북 반복하며 붙어있는 것들을 가져옴
# 8. 동서남북에 위치한 노드가 범위에 없으면 건너뛰기
# 9. 노드가 괴물이 아니고 한번도 방문 안한 곳일 경우
    # 큐에 연결된 위치 인덱스를 추가함
    # 미로배열 안 방문안한 위치의 노드 값을 붙어있었던 기본 x,y에 있는 거리값+1로 출발점에서의 거리값을 넣음
# 10. 모든 경우에 따라 1인 곳은 거리값이 되었기에 마지막 도착점에도 거리가 있을 것이다.
    # 따라서 도착점까지의 최단거리를 출력하면된다.