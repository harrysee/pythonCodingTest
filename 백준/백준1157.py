word = input().upper()
dic = {}
str = ''
for i in word:
    if i in dic.keys():
        continue
    dic[i] = word.count(i)

max = max(dic.values())
for i in dic.keys():
    if max == dic[i]:
        str+=i

if len(str)==1:
    print(str)
else:
    print('?')