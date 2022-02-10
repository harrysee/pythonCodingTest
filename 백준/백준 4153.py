# 각 변들의 길이가 3,4,5인 삼각형 = 직각삼각형
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오

import sys
lengths = list(map(int, sys.stdin.readline().split()))
while lengths[0]:
    key = lengths.index(max(lengths))
    if lengths.pop(key)**2 == lengths[0]**2+lengths[1]**2:
        print('right')
    else:
        print('wrong')
    lengths = list(map(int, sys.stdin.readline().split()))

# 해당 문제가 피타고라스의 정리를 활용하라는 건지 정확하게 이해하지 못하였고
# 피타고라스정리 : 가장큰수제곱 == 나머지1제곱+나머지2제곱
# 이공식이 한번에 안떠올라 헤맸다.ㅠㅠ 수학공부가 우선이다..
# 그래도 풀이는 배열에 길이들을 입력받고 가장 큰수의 위치를 찾아 저장한뒤
# 가장큰수를 배열에서 빼내며 나머지제곱 더한거와 비교하였다.
# [0, 0, 0]이 입력되면 중단하는 조건이 있어 첫번째수만 조건에 넣어주었다.