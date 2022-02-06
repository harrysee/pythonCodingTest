# 소수
# 자연수 M과 N이 주어짐
# M이상 N이하 자연수 중 소수인 것 찾기
# 소수의 합, 최솟값을 찾기
'''
    예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중
    소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
    이들 소수의 합은 620이고, 최솟값은 61이 된다.
'''

M = int(input())
N = int(input())
total = list()
for n in range(M, N+1):
    total.append(n)
    for i in range(2,n):
        if n%i==0:
            total.pop(-1)
            break

if M == 1: total.pop(0)
if len(total)==0:
    print(-1)
else:
    print(sum(total))
    print(total[0])

# 한줄평
# 소수라서 쉬울줄 알았는데 제한시간때문에 생각보다 어려웠다.
# 또한 M이 1일때는 제외해야헸기에 그부분도 if문을 써야해서 까다로웠다.
# 처음에는 소수일때 isSosu = True로 조건문을 줘서 배열에 넣었지만 시간제한에 걸렸다.
# 결국 배열에 넣고 소수가 아니면 배열에서 제외하는식으로 해결하였다.
# remove보다 pop이 효율적이였다.
# 최솟값은 인덱스 0이라는것을 뒤늦게 깨달았다.
# 나는 아직 잘 몰라서 if문을 굉장히 많이 썼지만 다른사람들의 효율적인 코드도 끝나고보니도움이됐다.

# 다른사람 풀이
# 소수가 나오는 공식을 이용하여 간결하게 푼 점이 신기했다
arr = [False, False] + [True] * 9999
for i in range(2, 101):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

m = int(input())
n = int(input())
nums = [i for i in range(m, n+1) if arr[i]]
print(sum(nums)if len(nums) else -1)
print(min(nums) if len(nums) else '')