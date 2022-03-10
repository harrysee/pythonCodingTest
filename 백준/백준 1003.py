# 피보나치 함수

# N번째 피보나치 수를 구하기
# 해당 함수를 이용하여 0과 1이 각각 몇 번 출력되는지 구하기
# 다이나믹 프로그래밍 사용하기
# 다른 자료를 참고하였다. 풀이 알고리즘 설명
    # 0과 1의 호출횟수를 구하는 것이 중점이다
    # 숫자마다 호출되는 횟수를 저장해나간다.
    # 입력한 숫자에서 감소하면서 찾는것이아닌
    # 처음부터 입력한 숫자까지 증가하면서 0,1의 호출횟수를 저장한다.

cnt0 = [1, 0, 1]
cnt1 = [0, 1, 1]
def fibonacci(n):
    length = len(cnt0)
    if n>=length:
        for i in range(length,n+1):
            cnt0.append(cnt0[i-1]+cnt0[i-2])
            cnt1.append(cnt1[i-1]+cnt1[i-2])
    return cnt0[n],cnt1[n]

t = int(input())
for i in range(t):
    zero,one =fibonacci(int(input()))
    print(zero,one)

# 다이나믹 프로그래밍에 대하여 충분한 학습이 필요하다고 본다.
# cnt0,cnt1을 입력받는 와중에도 계속하여 재사용을 하였다.
# 처음엔 cnt0,cnt1 의 가장 마지막 숫자를 출력하였는데 계속 재사용하는거라 마지막이 아닌
# 입력받은 수를 출력해야했다. cnt0,cnt1 [n]으로 바꿈