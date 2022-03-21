# 구현
# 문제) 도착지점 좌표를 출력하시오
# 크기 : NxN 정사각형의 (1,1) 지점에서 출발함
# L : 왼쪽한칸 / R:오른쪽한칸 / U:위쪽한칸 / D:아래한칸
# 조건) NxN 정사각형의 공간을 벗어나는 움직임은 무시된다.

# 초기풀이계획)
# 입력 : N
# 방향키배열 : dirs
# 변수 x,y(x=행/y=열)
# for - dirs
    # if문
    # L : y>1 -> y-1
    # R : y<N -> y+1
    # U : x>1 -> x-1
    # D : x<N -> x+1
# 출력 : x,y
import sys

N = int(input())
dirs = list( sys.stdin.readline().split())
x,y= 1,1

# 첫번째 풀이
for d in dirs:
    if d=='L' and y>1:
        y-=1
    elif d=='R' and y<N:
        y+=1
    elif d=='U' and x>1:
        x-=1
    elif d=='D' and x<N:
        x+=1

# 두번째 풀이
dx = [0,0,-1,1]
dy = [-1,1,0,0]
chk = ['L','R','U','D']
for d in dirs:
    nx,ny = x,y
    for i in range(len(chk)):
        if chk[i]==d:
            x += dx[i]
            y += dy[i]
            break
    if x<1 or x>N or y<1 or y>N:
        x,y = nx,ny
print(x,y)

# 첫번째 방법은 단순 if문 조건체크였다.
# 두번째는 책을 참고하였는데 방향 list를 사용하며 for문을 돌린 코드이다.
# 조건 체크는 나눠서 하지 않고 한번에 밑에서 하였다.
# 사실 개수나 문장만 본다면 1번방법을 dic으로 변형하던지 하는게 더 효율적일듯.