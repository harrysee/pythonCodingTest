# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
#
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

# dfs 를 활용한 코드
# 시간복잡도 계산 : n^3 + n logn
set_nums = set()
def is_sosu(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def dfs(numbers, num):
    set_nums.add(int(num))
    for i,n in enumerate(numbers):
        ns = list(numbers)
        ns.pop(i)
        dfs(ns,num+n)

def solution(numbers):
    answer=0
    for i,n in enumerate(numbers):
        ns = list(numbers)
        ns.pop(i)
        dfs(ns,f'{n}')
    for num in set_nums:
        if is_sosu(num):
            answer+=1
    return answer

# print(solution("17"))
# print(solution("011"))
print(solution("1231"))

# 초기의 for문만을 이용한 코드
import math

#
# def is_sosu(x):
#     if x <= 1: return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
#
#
# def solution(numbers):
#     answer = 0
#     nums = set()
#     for i, number in enumerate(numbers):
#         nstr = number
#         nums.add(int(nstr))
#         for j, num in enumerate(numbers):
#             if i == j:
#                 continue
#             nstr += num
#             nums.add(int(number + num))
#             nums.add(int(nstr))
#     print(nums)
#     for n in nums:
#         if is_sosu(n):
#             answer += 1
#     return answer

#
# [2, 3, 11, 13, 23, 31, 113, 131, 211, 311, 1123, 1213, 1231, 1321, 2113, 2131, 2311, 3121]
# {1, 2, 131, 3, 11, 12, 13, 21, 23, 31, 32, 3121, 311, 312, 321, 1231, 2131, 211, 213, 1123, 231, 112, 113, 121, 123}