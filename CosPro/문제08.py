def solution(characters):
   result = ""
   result += characters[0]
   for i in range(1, len(characters)):
       if characters[i - 1] != characters[i]:  # i가 0일 때 i-1 =-1 characters[-1]='e'
           result += characters[i]
   return result

#The following is code to output testcase. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

#보조문제
# arr ='abcdefg'
# # print(arr[len(arr)])
# print(arr[3])
# print(arr[6])
# print(arr[0])
# print(arr[-1]) #전체 길이 7에서 -1한다고 생각하면 됨
