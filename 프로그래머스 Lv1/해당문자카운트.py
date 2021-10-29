#어떤 문자열에 해당단어가 몇개 있는지 카운팅
str = "ILOVKEFLOVEE"
find ='LOV'
cnt = 0

# 일반화된 코드가 아닌지
# 결함을 찾기

for i in range(len(str)):
    if str[i] == 'L':
        if str[i+1] == 'O':
            if str[i+2] =='V':
                cnt+=1
print(cnt)

cnt=0
for i in range(len(str)):
    if str[i] == 'L' and i+len(find) <= len(str):
        if str[i+1] == 'O':
            if str[i+2] =='V':
                cnt+=1
