import sys
num = int(input())
r = 0
str = []
for i in range(num):
    R, S = sys.stdin.readline().split(" ")
    str.append(S)
    r = int(R)

for S in str:
    for s in S[:-1]:
        print((s * r), end='')
    print()