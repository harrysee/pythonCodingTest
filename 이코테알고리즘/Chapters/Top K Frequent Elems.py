# Top K Frequent Elems
# 자주 나오는 숫자들 찾기
import heapq
from collections import defaultdict
from typing import List

def topFrequent(nums:List[int], k:int) -> List[int]:
    if k==0:
        return []

    # hash map
    count_map = defaultdict(int)

    # count over nums
    for num in nums:
        count_map[num]+=1

    # fixed size heap
    topK_heap = []
    for num in count_map:
        heapq.heappush(topK_heap,(count_map[num],num))  #use hashmap count as comp
        if k < len(topK_heap):
            heapq.heappop(topK_heap)

    topk= []
    for count,num in topK_heap:
        topk.append(num)
    return topk

topK = topFrequent(nums=[1,3,5,3,9,3,7,5], k=2)
print(topK)

