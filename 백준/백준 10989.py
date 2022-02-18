# 수 정렬하기
# N개의 수가 주어졌을때 오름차순 정렬
# 메모리 초과, 시간초과를 주리며 코드 짜야됨
#mport sys
#
# n = int(sys.stdin.readline())
# num_list = []
#
# for _ in range(n):
#     num_list.append(int(sys.stdin.readline()))
#
# sorted_list = sorted(num_list)
#
# for i in sorted_list:
#     print(i)
# 이 코드는 메모리 초과가 난다. -> for문 속에서 append를 하면 메모리 재할당이 이루어져
# 메모리를 효율적으로 사용하지 못한다.
# 입력값이 크지않은 경우에는 상관없지만 입력값이 극한으로 많이 주어질때는 메모리관리 필요
# -> 미리 리스트 크기를 정해놓고 0번방부터 넣기
#파이썬은 내부적으로 연산과 메모리를 관리하기 때문에 파이썬에 내장되어있는 함수들을 적용할수록
# 메모리를 효율적으로 관리할 수 있다고 한다.
# 인덱스 활용 -> 크기의 인덱스에 +1해놓고 순회하며 1인 인덱스출력
import sys
nums = [0]*10001
t = int(input())

for _ in range(t):
    nums[int(sys.stdin.readline())] +=1

for i,n in enumerate(nums):
    if n==0: continue
    for j in range(nums[i]):
        print(i)

# 인덱스를 이용해서 메모리를 효율적으로 관리할수있다.
# for문에서 append를 쓰면 메모리할당이 계속 바뀌므로 훨씬 비효율적일수있다는 것을배웠다.
# 다른 코드를 참고했지만 인덱스를 이용해서 인덱스의 숫자로 출력하면 정렬을 하지 않아도 되서 좋은코드이다.
