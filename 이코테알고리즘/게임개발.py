# 구현 : 시뮬레이션
# 게임 캐릭터가 맵 안에서 움직이는 시스템
# 캐릭터 장소 1x1 크기의 정사각형이 NxM 크기 직사각형으로 있는 육지,바다임
# 조건1) 캐릭터 - 상하좌우 ㄱㄴ
# 조건2) 바다는 갈 수 없다.
# 움직임 메뉴얼 
    # 1. 현위치에서 현재 방향을 기준으로 왼쪽방향 90도씩부터 차례대로 갈 곳 선정
    # 2. 왼쪽 방향에 가보지 않은 칸 존재 시 왼쪽 회전 후 왼쪽 한칸 전진 / 왼쪽에 가보지 않은칸 없으면 회전만 수행, 1단계로
    # 3. 네 방향 모두 이미 가본 칸이거나 바다일 경우 바라보는 방향 유지, 한칸 뒤로가고 1단계로 돌아감 / 이때 뒤가 바다면 움직임 멈춤
# 움직임 멈출 때까지 반복적으로 수행하며 캐릭터가 방문한 칸의 개수 출력
# 입력 : 세로크기 N, 가로크기 M / 캐릭터 좌표 , 방향(동서남북:0123) / 육지|바다 정보(0|1)
import sys

# 입력받기
N,M = map(int, sys.stdin.readline().split())
x,y,dir = map(int, sys.stdin.readline().split())
maps = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

# 방향키
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 현위치 방문처리하기
maps[x][y] =1
cnt=1
turn_cnt = 0
while maps: # 움직일 칸이 현재일때 중지
    # 왼쪽으로 모든 방향 회전
    dir -=1
    if dir ==-1:
        dir =3
    # 한칸 전진
    nx = x+dx[dir]
    ny = y+dy[dir]
    if 0<nx<N and 0<ny<N and not maps[nx][ny]:
        x = nx
        y = ny
        cnt+=1
        turn_cnt =0
        maps[nx][ny] = 1
        continue
    # 전진 안될때
    turn_cnt +=1    # 방향 카운트(4방향되면 탈락)

    if turn_cnt >= 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if maps[nx][ny]:    # 뒤가 막혀있는 경우
            break
        x = nx
        y = ny
        maps[x][y] =1
        turn_cnt =0
print(cnt)

# 책과는 달리 maps 배열에서 직접적으로 방문 처리를 하는 비둘기집 알고리즘을 사용해봤다.
# 생각보다 문제가 까다로웠고
# 테크닉으로는 방향을 설정해서 이동하는 문제 유형에선 dx,dy를 방향순서에 맞게 방향키를 설정하여 재활용하는 것이 이득히다.
# turn_cnt를 통해 4번동안 안하면 중지하게 하는 것을 도움받았다.
# 초기에 cnt =1로 현위치를 방문처리 안해줘서 삽질 좀 했다...