# 같은 제품번호별로 장갑 각 몇쌍인지 구하기

max_product_number = 10
def func_a(gloves):
    counter = [0 for _ in range(max_product_number + 1)]
    for x in gloves:
        counter[x] += 1
        return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)

    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    return total


left_gloves = [2, 1, 2, 2, 4]
right_gloves = [1, 2, 2, 4, 4, 7]
ret = solution(left_gloves, right_gloves)

print('solution 함수의 반환 값은', ret, '입니다.')