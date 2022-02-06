#함수 선언
def sum_all(start, end):
    # 변수 선언
    out_put = 0
    # 반복문을 돌려 숫자 더하기
    for i in range(start, end + 1):
        out_put += i
    return out_put

print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))
