# 7.리스트에서 특정 원소만 추출하기
# 2를 제외한 나머지 추출
nums = [1, 2, 2, 2, 3, 1, 1, 3, 2]
result = list()
for n in nums:
    if n == 2:
        continue
    else:
        result.appand(n)
print(result)

