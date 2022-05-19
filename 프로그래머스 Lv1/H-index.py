# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
#
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
#
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

# def solution(citations):
#     max_idx = 0
#     for i in range(3):
#         max = citations[0]
#         max_idx =0
#         for j, ci in enumerate(citations):
#             if max> ci:
#                 max = ci
#                 max_idx = j
#         citations[max_idx] *=-1
#         print(citations)
#     return max_idx

def solution(citations):
    citations.sort(reverse=True)
    for i,cita in enumerate(citations):
        if i>=cita:
            return i
    return len(citations)

print(solution([5,3,3,8,10]))
print(solution([10,8,5,4,3]))
print(solution(	[3, 0, 6, 1, 5]))
print(solution(	[10, 10, 10, 10, 10]))
print(solution(	[0, 0, 0, 0, 0]))

# 다른 사람 풀이
# sort로 정렬해서 가장 큰값부터 작은값으로 정렬한후, enumerate로 (index, value)형태로 묶는다.
# 그리고 최댓값(start = 1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출하고,
# 이 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나온다.
# 이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나온다.
# 즉 h값들의 집합이나온다. h값중 최대값을 max로 뽑아서 출력하면 된다.
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer