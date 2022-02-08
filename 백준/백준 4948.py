# 자연수 n, n보다 크고, 2n보다 작거나 같은 소수 적어도하나는 존재
# 10< 소수 <=20 -> 4개
# n보다 크고 2n보다 작거나 같은 소수의 개수구하기
# 가우스의 공식을 이용 > 1부터 X까지 숫자 중 소수의 개수는(π(x)로 표시한다)
# X를 X 자릿수(99는 두 자릿수, 999는 세 자릿수)의 두 배로 나눈 값과 비슷하다는 것
# 첫번째 방법
# import sys
# limit = int(sys.stdin.readline())
#
# while limit:
#     x = round(limit/(len(str(limit))*2))
#     x2 = round(limit*2/(len(str(limit*2))*2))
#     print(x,x2,x2-x)
#     limit = int(sys.stdin.readline())

# 두번째 방법
# import sys
#
# limit = int(sys.stdin.readline())
#
# while limit:
#     if limit==1:
#         print(1)
#         limit = int(sys.stdin.readline())
#         continue
#     n2 = limit*2
#     if limit%2==1: limit+=1
#     cnt =0
#     for i in range(limit+1,n2+1,2):
#         cnt+=1
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 cnt-=1
#                 break
#     print(cnt)
#     limit = int(sys.stdin.readline())

# 세번째 방법

sosu = [2]
for i in range(3,246912,2):
    isSosu=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            isSosu-=1
            break
    if isSosu:
        sosu.append(i)

import sys
n = int(sys.stdin.readline())

while n:
    cnt=0
    index =0
    for s in sosu:
        if n< s <= n*2 :
            cnt+=1
    print(cnt)
    n = int(sys.stdin.readline())

# 제한조건 123456임으로 두배인 246912까지의 소수를 생성해야하는데 그걸 간과하여 삽질 좀 햇다..
# 첫번째는 그냥 틀리고 두번째는 시간제한에 걸렸다.