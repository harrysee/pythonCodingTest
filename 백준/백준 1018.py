# 체스판 다시 칠하기
# 각 칸이 검은색과 흰색 중 하나로 색칠되어있고, 변을 공유하는 두개의 사각형은 다른 색으로 칠해져 있어야함
# 체스판을 색칠하는 경우 : 맨 왼쪽 위칸이 흰색인 경우, 하나는 검은색인경우
# 8*8 크기의 체스판으로 잘라낸 후에 몇개의 정사각형을 다시 칠해야됨
# 8*8 크기는 아무데서나 골라도 된다.
# 지민이가 다시 칠해야하는 정사각형의 최소 개수를 구하기

# 힌트 : 체스판의 시작이 흰색이거나, 검은색이거나 둘 중 하나 = 첫시작이 B이면 행인덱스+열인덱스는 모두 B여야함
# https://god-gil.tistory.com/62
# 계획
# 입력
# 체스판 입력받기 이차원배열

# 참고한 코드
# 4중 for문
# 처음부터 끝까지 8개씩만 가져올수있도록 나머지 여분 8개가 남도록 N,M-7해서 고정해줌
# 고정한 후 각각 끝까지 인덱스를 이동시키며 
# 행인덱스 + 열인덱스가 짝수,홀수인경우 앞의 컬러를 유추해서 배열에 저장
N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

for i in range(N - 7):
    for j in range(M - 7):
        first_W = 0
        first_B = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W + 1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W + 1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)
print(min(repair))
# print(min(re))

# 이번문제는 좀 난이도가 있어서 다른 코드를 참고했다.
# 각 8개의 모든 경우를 돌아보며 가장 적게 바꿔야할 개수를 min()함수로 구하였다.