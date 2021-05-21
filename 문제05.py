def solution(number):
   count = 0
   for i in range(1, number + 1):  # for(int i=1; i<number+1)
       current = i
       temp = count
       while current != 0:
           # if current%10==3 or current%10 ==6 or current%10==9
           if current%10 in [3,6,9]:
               count += 1
               print("pair", end = '') # 디버깅을 위한 출력(없어도 무관)
           current = current // 10
       if temp == count:  # 3,6,9에 포함이 되지 않을 때
           print(i, end = '') # 디버깅을 위한 출력(없어도 무관)
       print(" ", end = '') # 디버깅을 위한 출력(없어도 무관)
   print("") # 디버깅을 위한 출력(없어도 무관)
   return count

#The following is code to output testcase.
number = 40
ret = solution(number)
print(f'{ret}번 박수침')