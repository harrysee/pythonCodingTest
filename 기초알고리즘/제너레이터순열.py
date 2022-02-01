## 제너레이터를 이용해서 조합 구현 (중복 조합 X)
def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:], r-1):
                yield [array[i]] + next

print("\n\ncombinations 직접 구현")
for i in combinations_2([1,2,3,4], 3):
    print(i, end=" ")

# 순열 ------------------------------------
def permutations_2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations_2(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

for i in permutations_2([1,2,3,4],2):
    print(i, end=" ")


# -------- 중복없는 조합 ---------
def combine(arr, r):
    for i in range(len(arr)):
        if r== 1:
            yield [arr[i]]
        for next in combine(arr[i+1:],r-1):
            yield [arr[i]] + next

for i in combine([1,2,3,4],3):
    print(i)



# 소수 ==============
def is_prime(x):
    for i in range(2,x):
        if x%i == 0 :
            return False
    return True