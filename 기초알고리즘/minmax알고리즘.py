
max = -1
min=1000
nums = [3,6,2,7]
for n in nums:
    max = n if n>max else max
    min = n if n<min else min

print(max, min)