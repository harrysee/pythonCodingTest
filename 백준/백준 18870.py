# 좌표압축
# 수직선 위 N개의 좌표 x1,x2,x3,,,xN
# xi를 좌표 압축 -> x'i값 = xi>xj를 만족하는 서로 다른 좌표 개수와 같음
# x1,x2,,,xn에 좌표 압축을 적용한 결과 x'1,x'2...출력
# 2 4 -10 4 -9 -> 2 3 0 3 1

# 계획
# 정렬시키기
# 중복제거 set
# set을 돌며 해당 숫자 인덱스를 해당숫자와 함께 딕셔너리 넣기
# 출력 해당 숫자에 맞는 딕셔너리 값 출력하기

import sys
n = int(input())
dots = list(map(int,sys.stdin.readline().split()))
index ={}

for i,s in enumerate(sorted(set(dots))):
    index[s] = i

for d in dots:
    print(index[d],end=" ")

# 해결) 처음에 입력이 한칸씩 띄워서 들어오는지모르고 for문돌려서 입력받다가 아차함
# 리스트로 바로 입력받고 중복없이 정렬시킨 후 딕셔너리에 개수랑 바로바로 담음
# 시간이 좀 걸렸지만 다양한 파이썬 옵션을 이용해 해결