#arr의 수 세기
''''
1단계. 리스트에 들어있는 각 자연수의 개수를 셉니다.
2단계. 가장 많이 등장하는 수의 개수를 구합니다.
3단계. 가장 적게 등장하는 수의 개수를 구합니다.
4단계. 가장 많이 등장하는 수가 가장 적게 등장하는 수보다 몇 배 더 많은지 구합니다.
~~~'''
import math
def 보조함수_a(arr):
   counter = [0 for _ in range(1001)]
   for x in arr:
       counter[x] += 1
   return counter

def 보조함수_b(arr):
   ret = 0
   for x in arr:
       if ret < x:
           ret = x
   return ret

def 보조함수_c(arr):
   INF = 1001
   ret = INF
   for x in arr:
       if x != 0 and ret > x:
           ret = x
   return ret

def solution(arr):
   counter = 보조함수_a(arr)
   max_cnt = 보조함수_b(counter)
   min_cnt = 보조함수_c(counter)
   return max_cnt // min_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)
print(ret)
