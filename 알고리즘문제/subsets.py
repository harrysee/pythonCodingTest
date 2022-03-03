# 백트래킹
# 문자열을 받아 문자열에 속해있는 서브문자열들 출력
# abc -> a, ab, ac, b, bc, c
inputstr = input()
output= list()
def BT(index, letters): # 반복될 함수
    global output
    # 마무리할 조건 : 리턴
    if index==len(inputstr):
            output.append(letters)
            return
    # 처리부분 : 여기서는 인덱스에 맞는 문자를 가져옴
    c = inputstr[index]
    # 나아가면 트리구조확장시키며 추가되는 파트
    BT(index+1,letters+c)
    BT(index+1,letters)

# 출력
BT(0,'')
for o in output:
    print(o)