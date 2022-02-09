# 소인수분해
# 2로 나눈다
# 3으로 나눈다.
# 2~N까지 N을 나눈다.
# 2~N까지 나눠지지않으면 +1
# 나눠지면 N에 나누고 난 숫자를 업데이트
# 마지막에 나눠지지않은 숫자도 소인수기에 출력

def solution(N):
    d = 2
    while d<N:
        if N%d==0:
            N //=d
            print(d)
            continue
        d+=1
    if N >= 1:
        print(N)

solution(int(input()))

# 한줄평
# for문 2~N까지로 할까했는데 while문에서 2로 나눠지지않으면 +1하는게 힌트였다.
# 시간복잡도가 O(n log n)인듯하여 다소 시간이 오래걸린점을 생각해봤다.
# -> while문에 N을 계속 감소시켜 시간복잡도를 감소시키려했지만 그래도 오래걸려서 아쉽다.
# 생각해보니까 1 체크를 할필요가없었다... 아무것도 출력안함이니까 1보다크면 print(N)으로 바꿔줬다.

# 다른사람코드 - 나도 이런식으로 할까했는데 오래걸릴거같아서 안했다. 근데 ㄱㅊ할지도
n = int(input())
i = 2
r = int(n ** 0.5)

while i <= r:
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)