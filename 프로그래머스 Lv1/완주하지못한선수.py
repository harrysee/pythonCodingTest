# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
# 완주한 선수들의 이름이 담긴 배열
# completion이 주어질 때, 완주하지 못한 선수의 이름을
# return 하도록 solution 함수를 작성해주세요.

def solution(participant, completion):
    # 첫번째 풀이 - 효율성 떨어짐
    for c in completion:
        participant.remove(c)
    return participant[0]

def solution2(participant, completion):
    participant.sort()
    completion.sort()
    for i, c in enumerate(completion):
        if c != participant[i]:
            return participant[i]
    return participant[-1]

# 해시함수 사용한 예제
# 해석 : 같은 문자열에는 같은 해쉬가 적용된다
def solution3(participant, completion):
    answer = ''
    temp = 0
    dic = dict()
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer

s1 = solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
s2 = solution2(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
s3 = solution3(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
print(s1)
print(s2)
print(s3)
