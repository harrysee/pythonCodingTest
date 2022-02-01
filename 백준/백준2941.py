word = input()
croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0

for cr in croa:
    num = word.count(cr)
    for _ in range(num):
        word = word.replace(cr, "")
    cnt+=num
print(cnt+ len(word))