h,m = map(int, input().split())
mm = int(input())

h+=(m+mm)//60
m = (m+mm)%60

if h>=24: h-=24
print(h,m)

# h가 24일때 0만 고려하고 h가 24가 넘어가면 24를 빼줘야한다는 걸 고려하지 못해
# 애먹었다. 문제를 찬찬히 확실히 이해해야겠다.

