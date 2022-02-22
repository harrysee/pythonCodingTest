# 단어 정렬
# 알파벳 소문자로 이루어진 N개의 단어
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전순으로
# 조건 ) 문자열 길이 <=50, 중복단어제외

import sys
#
# t = int(input())
# words = list()
# for i in range(t):
#     words.append(sys.stdin.readline()[:-1])
# words.sort(key=lambda x:(len(x),x))
# for w in words:
#     print(w)

# 이전코드임.. 조건 중복제외를 확인못해서 list로 했다가 걸림
# 처음에는 x[0]으로 첫번째 단어만 비교해버려서 수정하긴햇음
# ----------------

t = int(input())
words = set()
for i in range(t):
    words.add(sys.stdin.readline()[:-1])
words = sorted(words,key=lambda x:(len(x),x))

for w in words:
    print(w)

# 코드 풀이
# 파이썬 sort 옵션을 사용하면 왠만한 정렬기능은 쉽게 구현이 가능하다.
# 파이썬 다중정렬을 위해 정렬 key를 첫번째 문자열길이, 두번째 문자열 로 이차정렬을 하였다.
# 중복 제거를 위해 처음부터 set을 사용하였다.