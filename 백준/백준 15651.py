# N과 M (3)
# 1~N 중 M개를 고른 수열
# 중복 가능 순열

# product 사용
from itertools import product
N,M = map(int,input().split())

for n in product(range(1,N+1),repeat=M):
    for i in n:
        print(i,end=' ')
    print()

# product 매개변수로는 범위,[범위(문자열 등)],[뽑을개수]이다.
# 같이 섞어쓸 범위를 가변으로 입력받아 repeat를 키워드로 주지않으면 인식안해줌
# 이부분을 새로 알게되었다.