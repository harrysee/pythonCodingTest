# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

cnt =0
nums, key = [],0
def solution(numbers, target):
    global nums,key,cnt
    nums= numbers
    key = target
    number(0, 0, 0)  # 마이너스
    number(0, 1, 0)  # 플러스
    return cnt//2

def number(idx, giho, result):
    global cnt
    # print(idx, len(nums),giho, cnt)
    if idx >= len(nums):
        if result==key:
            cnt+=1
            print('-> ',idx,result,cnt)
        return
    n = nums[idx]
    if giho == 0:   # 마이너스
       n*=-1
    value = n+result
    print('기호 :',giho,'값:',nums[idx],value)
    number(idx+1, 0, value) # 마이너스
    number(idx+1, 1, value) # 플러스
    return

# 다른 풀이
# 배열을 하나씩 빼서 앞에꺼랑 더해서 구하는 것이 아닌 타겟에서 빼서 구하는 것으로 함
# 그냥 솔루션을 이용한게 존경스러운 풀이방법
def solution1(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
