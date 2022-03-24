# DFS/BFS
# N x M 크기의 얼음 틀
# 구멍이 뚫려있는 부분은 0 / 칸막이가 존재하는 부분은 1
# 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어있는 경우 서로 연결되어 있는 것으로 간주
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하여라
# 입력 : 얼음틀의 세로 길이 N, 가로길이 M이 주어짐 / 두번째줄 : 얼음틀의 형태 주어짐

# 풀이 계획
# 2차원 배열 형태의 그래프로 인식한다.
# 상하좌우로 DFS로 각각 탐색하며 붙어있는 0인곳에 가서 방문체크 한다.
# 0이 아니면 무조건 FALSE로 반환
# 그래프 전체를 한개씩 전부 for문 돌리면서 함수 호출하고 True로 반환하는 것만 카운트

import sys
N, M = map(int, input().split())
ices = []
for i in range(N):
    ices.append(list(map(int, sys.stdin.readline().split())))

# 0이 붙어있는 곳을 모두 체크할 함수
def check_ice(x,y):
    global ices
    if x>=N or x<0 or y>=M or y<0:
        return False

    if not ices[x][y]:
        ices[x][y] =1

        # 붙어있는 0인 곳들을 모두 방문처리한다. DFS : 재귀
        check_ice(x-1,y) # 상
        check_ice(x+1,y) # 하
        check_ice(x,y-1) # 좌
        check_ice(x,y+1) # 우
        return True
    return False

count=0
for i in range(N):
    for j in range(M):
        if check_ice(i,j):
            count+=1
print(count)

# 이차원 리스트를 그래프를 만든다는 것이 잘 이해가 안됐는데 문제를 풀면서 상하좌우를 탐색하는 방법을 배웠다.