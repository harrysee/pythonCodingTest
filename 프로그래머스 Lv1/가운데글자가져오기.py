def solution(s):
    a = len(s)//2
    if len(s)%2==0:
        return s[a-1:a+1]
    else:
        return s[a]

s1 = 'abcdeaa'
print(solution(s1))
s2 ="qwer"
print(solution(s2))