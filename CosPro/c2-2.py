def func_a(arr):
    count = 0
    for n in arr:
        if n % 5 == 0:
            count += 1
    return count


def func_b(three, five):
    if three > five:
        return "three"
    elif three < five:
        return "five"
    else:
        return "same"


def func_c(arr):
    count = 0
    for n in arr:
        if n % 3 == 0:
            count += 1
    return count

def solution(arr):
    count_three = func_c(arr)
    count_five = func_a(arr)
    answer = func_b(count_three,count_five)
    return answer

arr = [2, 3, 6, 9, 12, 15, 10, 20, 22, 25]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")