# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
#
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
#
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
#
# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

# 예제 1)
# progresses : [40, 93, 30, 55, 60, 65]
# speeds : [60, 1, 30, 5 , 10, 7]
# return : [1,2,3]
#
# 예제 2)
# progresses : [93, 30, 55, 60, 40, 65]
# speeds : [1, 30, 5 , 10, 60, 7]
# return : [2,4]

import math
from collections import deque

# 문제 이해를 참고해서 top에 앞에 값을 담아서 푼 코드
def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        answer.append(math.ceil((100 - progresses[i]) / speeds[i]))
    # print(answer)

    answer = deque(answer)
    top = 0
    for i in range(0, len(answer)):
        if top < answer[i]:
            top = answer[i]
            days.append(1)
        else:
            days[-1]+=1
    return days

print(solution([40, 93, 30, 55, 60, 65],[60, 1, 30, 5 , 10, 7]))
print(solution([93, 30, 55, 60, 40, 65],[1, 30, 5 , 10, 60, 7]))

import math


# 내 원래 코드
#
def solution1(progresses, speeds):
    answer = []
    days = [1]
    for i in range(len(progresses)):
        answer.append(math.ceil((100 - progresses[i]) / speeds[i]))

    top = 0
    for i in range(1, len(answer)):
        if answer[i - 1] >= answer[i]:
            answer[i]= answer[i-1] # 이 코드가 없어서 틀렸다
            # -> 바로 앞에거랑만 비교하는 줄 알았는데 그냥 '앞'에보다 빨리 끝나면 같이 배포였다.
            # 문제이해만 잘했어도 맞았을듯..
            days[top] += 1
        else:
            top += 1
            days.append(1)
    return days


print(solution1([40, 93, 30, 55, 60, 65],[60, 1, 30, 5 , 10, 7]))
print(solution1([93, 30, 55, 60, 40, 65],[1, 30, 5 , 10, 60, 7]))

from math import ceil

# 참고하여 공부한 코드
def solution(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList