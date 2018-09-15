from heapq import heappop, heappush , heapify

heap = []
nums= [12,3,-2,6,4,8,9]
"""
for i in nums:
    heappush(heap, i)

while heap:
    print(heappop(heap))
"""
heapify(nums)

print(nums)
