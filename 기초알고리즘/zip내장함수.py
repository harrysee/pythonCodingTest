# 8. zip을 사용하는 반복문 예시
# zip : 두개를 병렬로 묶어서 반환함
# 한개씩 묶고 개수가 맞지 않으면 따로 처리함
arr1 = [1,2,3]
arr2 = [10,20,30,40]

for z in zip(arr1, arr2):
    print(z)

# zip 코드 직접 짜보기
for i in range(min(len(arr1),len(arr2))):
    print(f'({arr1[i]}, {arr2[i]})')