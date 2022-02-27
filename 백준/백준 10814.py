# 나이순 정렬
# 가입한 사람들의 나이와 이름이 가입한 순서대로 주어짐
# 1. 나이 오름차순
# 2. 가입한 순서 오름차순
# 조건 : 온라인 저지 회원을 한명씩 "나이 이름"으로 출력

import sys
n = int(input())
users = [[0,""] for i in range(n)]
for i in range(n):
    users[i][0],users[i][1] = sys.stdin.readline().split()
    users[i][0] = int(users[i][0])

users.sort(key= lambda x:x[0])
for user in users:
    print(user[0],user[1])

# 풀이 : 입력 길이가 길어질수 있기 때문에 길이고정된 배열 미리 선언
# 일차원 배열 구성 : [가입순서, 나이, 이름]
# 파이썬 정렬옵션으로 나이정렬 후 가입순서(입력받은인덱스)로 정렬하였다.

# 처음에 int(users[i][0])만 기재하였다.
# 그러나 int형변환은 비파괴적처리였기에 int형으로 당연히 바뀌지않음
# users[i][0] = int(users[i][0]) 이렇게 바꿔주니 됨..