
import sys
all =[]
x,y = map(int,sys.stdin.readline().split())

while x:
    all.append([x,y])
    x, y = map(int, sys.stdin.readline().split())

print(len(all))
for i,a in enumerate(all):
    print(f'shapes[{i}][0]={a[0]}; shapes[{i}][1]={a[1]};')