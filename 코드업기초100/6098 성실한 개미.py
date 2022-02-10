import sys
box = []
for _ in range(10):
    box.append(list(map(int, sys.stdin.readline().split())))

x = 1
y = 1
while box[x][y]!=2:
    box[x][y]=9
    next = box[x][y+1]
    if next != 1:
        y+=1
    elif box[x+1][y]==1:
        break
    else:
        x+=1

box[x][y]=9
for bx in box:
    for b in bx:
        print(b,end=' ')
    print()