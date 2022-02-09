# 네번째 점
# 세점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네번째 점을 찾는 프로그램
# 세 점의 좌표가 한줄에 하나씩 주어짐
# x축 = 같은 두개 빼고 같지 않은 한개찾기
# y축 = 다른 한가지 숫자 찾기
import sys
x, y = [],[]
rx, ry = 0,0
for _ in range(3):
    w,h = map(int,sys.stdin.readline().split())
    x.append(w)
    y.append(h)

for w,h in zip(x,y):
    if x.count(w)==1: rx = w
    if y.count(h)==1: ry = h

print(rx,ry)

# 이거보다 좀 더 효율적으로 할수있지않을까 하는마음에 삽질하다가 좀 오래걸렸다
# for문을 3번이나 두번써서 O(3n)*3 이 걸린것같다
# for문을 두번째에 돌리지않고 find를 써서 인덱스를 비교하며 구하는 방법도 생각해보았다.