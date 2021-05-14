def solution(arr):
    left  = 0
    right= len(arr) - 1
    
    #TODO : @@@ 빈칸 채우기
    while left < (len(arr)/2):
        #arr[left]와 arr[right]의 값을 치환
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# The following is code to output testcase.
arr = [1, 4, 2, 3]  # input arr
ret = solution(arr)

# Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")
