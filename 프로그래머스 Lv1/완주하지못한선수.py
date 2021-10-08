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

s2 = solution2(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
print(s2)
