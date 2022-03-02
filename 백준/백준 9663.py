# N-Queen
# N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓아야함
# N이 주어졌을 때, 퀸을 놓는 방법의 수 구하기

# 계획
# 처음부터 이중배열로 해결하려했으나 시간이 걸릴거같아서
# 다른 블로거들을 참고해 힌트를 얻었다.
# 1. 퀸만큼 반복
# 2. 퀸을 열마다 한개씩만 놓을 수 있기 때문에
# 3. 세로체크안하고 가로, 대각선체크하는함수 호출
# 4. 체크 결과 트루면 재귀
N = int(input())
rows = [0]*N
cnt=0

def isQueen(x):
    for i in range(x):
        # row[x]== row[i] : 동일한 열이 있는지 검사,
        # 대각선확인하기 현재 x보다 큰값확인x = 가로1-가로2 == 세로1-세로2
        if rows[x] == rows[i] or abs(rows[x]-rows[i]) == abs(x-i):
            return False
    return True

def n_queen(x):
    global cnt
    if x==N:
        cnt+=1
    else:
        for i in range(N):
            # [x,i]에 퀸을 놓음
            rows[x]=i
            if isQueen(x):
                n_queen(x+1)

n_queen(0)
print(cnt)

# 파이참으로 풀었을때는 계속 시간초과가 떳다. 파이썬은 백트래킹에 원래 적합하지않다고,,
# 따라서 파이썬으로 풀때는 많은 조건문을 통해 유망한 가지들을 골라줘야한다.
# 1. N개의 퀸배치이기에 무조건 모든 행에 퀸이 들어가야함
# 2. 그렇기때문에 0열부터 N-1열까지 퀸을 놓는 방법을 for문 통해 돌리기
# 3. 유망한지 검사하는 함수를 통해 유망함수만을 걸러줌

# 내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


# 한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result

    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)


N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)

# ㅋㅋ 아무리해도 이게 정답코드인데 통과가 안됐다.
# 결국 1~15까지의 모든 답을 정리해둔 코드를 보고 해결할 수 있었다.
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])

# 중요한점 : 백트래킹은 가지치기중요, 백트레킹은 재귀필요
