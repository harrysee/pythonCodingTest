
# import sys
# all =[]
# x,y = map(int,sys.stdin.readline().split())
#
# while x:
#     all.append([x,y])
#     x, y = map(int, sys.stdin.readline().split())
#
# print(len(all))
# for i,a in enumerate(all):
#     print(f'shapes[{i}][0]={a[0]}; shapes[{i}][1]={a[1]};')

import sys
all =[]
strr = sys.stdin.readline().strip()
i=1

while strr:
    if i%2:
        st = strr.find("(")
        end = strr.find(")")
        x,y= map(int, strr[st+1:end].split(", "))
        print(i,x,y,"pass")
        all.append([x,y])
    strr = sys.stdin.readline().strip()
    i+=1

print(len(all))
for i,a in enumerate(all):
    print(f'shapes[{i}][0]={a[0]}; shapes[{i}][1]={a[1]};')

drowing = [[0 for i in range(100)] for i in range(100)]
for x,y in all:
    drowing[y][x] ="o"

for drow in drowing:
    for d in drow:
        if d:
            print(d,end='')
        else:
            print(" ",end='')
    print()