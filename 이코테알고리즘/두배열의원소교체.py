# 정렬 : 두 배열의 원소 교체
# 1. 두개의 배열 A, B는 N개의 자연수 원소로 구성,
# 2. 최대 K번의 바꿔치기 연산 수행 : 배열 A연산 한개 <-> 배열 B 원소 한개 바꾸는 것을말함
# 3. 목표 : A의 모든 원소의 합이 최대가 되도록 하는 것
# 입력 : N,K, 배열 A,B 가 주어짐
# 조건 : 배열크기 : 최대 100000 / K 최대 : N
# 아이디어 : 배열 A의 가장 작은 원소 <-> 배열 B의 가장 큰 원소 바꾸는 작업 K번 하여 최댓값 출력하기
import sys

N,K = map(int, sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
A.sort()    # A는 작은수부터 앞에 오게
B.sort(reverse=True)    # B는 큰수부터 앞에 오게

for k in range(K):
    if A[k] > B[k]: break # A의 작은수가 B의 큰수보다 클 경우를 고려한다.
    A[k],B[k]= B[k],A[k]

print(sum(A))

# 최대 100000이므로 O(N log N)으로 짜야했다
# 일단 큰수 작은수는 앞으로 정렬하고 구하는것이 훨씬 효율적이며 다양한 경우도 고려해야함