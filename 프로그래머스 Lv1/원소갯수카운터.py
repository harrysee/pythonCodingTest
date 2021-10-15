def solution(n):
    cnt = 0
    for i in n:
        if i==2:
            cnt+=1
    print(cnt)
solution([1, 2, 2, 2, 3, 1, 1, 3, 2])