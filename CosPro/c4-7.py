'''점수가 가장많이 오른 학생의 점수 차이와 가장 많이 떨어진 학생의 점수 차이 구하기
    한줄바꾸기
'''
def func_a(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = max(answer, score2 - score1)
    return answer

def func_b(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = min(answer, score1 - score2)
    return answer

def solution(mid_scores, final_scores):
    up = func_a(mid_scores, final_scores)
    down = func_b( final_scores,mid_scores)
    answer = [up, down]
    return answer

mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)

print("solution 함수의 반환 값은", ret, "입니다.")