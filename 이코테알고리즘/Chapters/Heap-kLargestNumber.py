# K largest numbers
# 배열 속 3개의 큰수를 출력
import heapq

nums = [1,3,5,7,9,11]
print(nums)

large_nums = []

for num in nums:
    heapq.heappush(large_nums,num)
    if 3<len(large_nums):
        heapq.heappop(large_nums)

print(large_nums)

# heapq.heapify(nums)
# heapq.heapify(nums)
# print(nums)

from typing import List

#make parent node largest
def swap(arr:List[int], rootIdx:int):
  largeIdx = rootIdx
  leftChild = 2 * rootIdx + 1
  rightChild = 2 * rootIdx + 2

  if leftChild < len(arr) and arr[largeIdx] < arr[leftChild]:
    largeIdx = leftChild

  if rightChild < len(arr) and arr[largeIdx] < arr[rightChild]:
    largeIdx = rightChild

  if largeIdx != rootIdx:
    arr[rootIdx], arr[largeIdx] = arr[largeIdx], arr[rootIdx]

    # recursive call to child
    swap(arr,largeIdx)

def heapify(arr:List[int]):
  for idx in range(len(arr)//2,-1,-1):
    swap(arr=arr,rootIdx=idx)

arr = [1,3,5,7,9,4,6]
heapify(arr)
print(arr)