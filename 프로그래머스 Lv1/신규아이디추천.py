def solution(new_id):
    new = ''
    if len(new_id) == 0:
        # 15자까지 제거
        new = 'a'
    elif len(new_id) > 15:
        new_id = new_id[:15]
    # 체크
    new = no_char_check(new_id)
    if '.' in (new_id[0], new_id[-1]):
        new_id[0], new_id[-1] = '', ''
    if len(new_id) < 2:
        k = new_id[-1]
        while len(new_id) < 3:
            new_id += k
    return new

def no_char_check(id):
    nochar = ['-', '_', '.']
    cnt=0
    for i in range(len(id)):
        if id[i].isalpha() and not id[i].islower():
            id[i] = id[i].upper()
        elif not id[i].isalpha() and not id[i].isdigit() and id[i] not in nochar:
            id[i] = ''
        elif id[i]=='.':
            cnt+=1
            if cnt>=1: id[i]=''
        else:
            cnt=0
    return id

str = input()
print(solution(str))