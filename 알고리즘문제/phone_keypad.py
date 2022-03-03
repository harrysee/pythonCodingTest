# 백트래킹 
# 가지치기하면서 안되는 수가 있으면 다시 돌아가고
# 맞는 곳으로 모든 경로를 탐색하는 것
# 전화번호를 입력하면 모든 조합을 계산하기
# 재귀

num = input()
output = list()
keys = ['','','ABC','DEF','GHI','JKL','MNO','RQRS','TUV','WXYZ']

def bt(index, letter):
    global output
    if index >= len(num):
        output.append(letter)
        return
    n = int(num[index])
    chars = keys[n]

    for c in chars:
        bt(index+1,letter+c)
        letter.replace(c,'')

bt(0,'')
for o in output:
    print(o)
