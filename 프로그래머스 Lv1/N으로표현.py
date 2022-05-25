
def solution(n,Number):
    dist = [list() for _ in range(8+1)]
    dist[1].append(n)
    dist[2].append({n, n * n, n // n, n + n, n - n})
    if Number in dist[1]:
        return 1
    elif Number in dist[2]:
        return 2

    for i in range(3, 8+1):
        temp = set()
        temp.add(int(n*i))
        for j in range(1,i):
            for k1 in dist[i]:
                for k2 in dist[i - j]:
                    temp.add(k1+k2)
                    temp.add(k1*k2)
                    if k1 and k2:
                        temp.add(k1-k2)
                        temp.add(k1//k2)
        if Number in temp:
            return i
        dist[i].append(temp)

    return -1
print(solution(5,12))
def calculate_n(X, Y):
    n_set = set()
    for x in X:
        for y in Y:
            n_set.add(x+y)
            n_set.add(x-y)
            n_set.add(x*y)
            if y != 0:
                n_set.add(x//y)
    return n_set

def solution1(N, number):
    answer = -1
    result = {}   # key는 숫자 사용횟수, value는 숫자를 key번 사용했을 때 나오는 연산 결과셋
    result[1] = {N} # N을 1번 사용할 때는 그냥 N
    if number == N:
        return 1
    for n in range(2, 9):  # 8번까지만 계산하므로
        i = 1
        temp_set = {int(str(N)*n)}  # N=5, 2번 사용할 때 먼저 55를 저장
        # 1 (op) N-1.... n-1 (op) 1 까지 계산
        while i < n:
            temp_set.update(calculate_n(result[i], result[n-i]))
            i += 1
        # 만들어진 셋에 원하는 숫자가 있으면 stop
        if number in temp_set:
            answer = n
            break

        result[n] = temp_set

    return answer