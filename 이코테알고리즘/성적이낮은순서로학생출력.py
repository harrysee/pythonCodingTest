# 정렬
# N명의 학생 정보 : 이름 성적
# 성적이 낮은 순서대로(오름차순) 학생의 이름을 출력하는 프로그램 작성
# 조건) 학생수 범위 : 1~100000 / 성적범위 : 1~100
import sys

N = int(input())
students = []

for i in range(N):
    students.append(tuple(sys.stdin.readline().split()))
students = sorted(students, key=lambda x:int(x[1]))
for s in students:
    print(s,end=' ')
# 파이썬 라이브러리의 key에 람다함수를 적용하여 해결하였다.
# 계수 정렬로도 풀 수 있는데 계수 정렬은 1~100까지 배열을 초기화하고 해당 점수의 학생인덱스를 추가하는 방식을 쓰면 좋을 것이다.

