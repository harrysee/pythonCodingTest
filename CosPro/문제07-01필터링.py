sentence1="never odd or.. even"

str = ''
# 문자열에 있는 원소 하나하나 꺼내기
for x in sentence1:
    if x != ' ' and x !='.':
        str+=x

print(str)