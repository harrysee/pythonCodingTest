# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다.
# 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
from collections import deque


def solution(begin, target, words):
    q = deque()
    q.append((begin,0))
    visited = [0 for i in range(len(words))]
    while q:
        word, cnt = q.popleft()
        print(cnt)
        if word == target:
            return cnt
        for idx, w in enumerate(words):
            count=0
            if not visited[idx]:
                for i in range(len(w)):
                    if word[i] != w[i]:
                        count+=1
                if count==1:
                    visited[idx] = 1
                    q.append((w, cnt+1))
    return 0

print('결과' ,solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
# solution("hit","cog",["hot", "dot", "dog", "lot", "log"])