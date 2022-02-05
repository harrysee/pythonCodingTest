# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)
# 출력
# 첫째 줄에 A+B를 출력한다.

import sys
a,b = map(int, sys.stdin.readline().split())
print(a+b)

# 한줄평 : 쉬어가는 단계같았다.
# 파이썬엔 그냥 long이 없이 int범위를 넘어가는 정수도 type int로 취급한다는것을 다시 알게됐다..