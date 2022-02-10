import sys
h,w = map(int, sys.stdin.readline().split())
n = int(input())
dots = [[0 for _ in range(w)] for _ in range(h)]

for i in range(n):
    l,d,x,y = map(int,sys.stdin.readline().split())
    if d:
        for j in range(x-1,x+l-1):
            dots[j][y-1] = 1
    else:
        for j in range(y-1,y+l-1):
            dots[x-1][j]=1

for dot in dots:
    for d in dot:
        print(d,end=' ')
    print()