A, B, C = tuple(map(int, input().split()))
b, c = A, 0
count = 0

if B < C:
    print(-1)

while c < b:
    b += B
    c += C
    count += 1
print(count)
