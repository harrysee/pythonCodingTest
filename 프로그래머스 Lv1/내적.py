def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

aa = [1,2,3,4]
bb = [-3,-1,0,2]
print(solution(aa,bb))