# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
#
# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

# 보완한 풀이
# 값을 위주로 정렬하였기 때문에 현재 넘버가 뒷 번호의 접두어에 있는지만 체크하도록 하였다.
# 관련된 파이썬 함수로는 startswith가 있다.
# startswith : a.startswith(b)
# -> a의 시작부분이 b로 시작하면 True 반환 아니면 False 반환
# 인자값으로는 문자열, 문자열로 이루어진 튜플밖에 안된다.
# def solution(phone_book):
#     return getBool(phone_book)

def getBool(phone_book):
    phone_book.sort()  # 오름차순 정렬
    for i,phone in enumerate(phone_book[:-1]):
        # print(phone, phone_book[i+1][:(len(phone))])
        if phone == phone_book[i+1][:(len(phone))]:
            return False
    return True

def solution(phone_book):
    phone_book.sort()
    for ph1, ph2 in zip(phone_book, phone_book[1:]):
        if ph2.startswith(ph1):
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))

# # 첫번째 풀이
# def getBool(phone_book):
#     phone_book.sort(key=lambda x: len(x))  # 오름차순 정렬
#     for i, word in enumerate(phone_book[:-1]):
#         slice = len(word)
#         for phone in phone_book[(i + 1):]:
#             if word == phone[:(slice)]:
#                 return False
#     return True
#
# def solution(phone_book):
#     return getBool(phone_book)