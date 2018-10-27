import heapq
from heapq_heapdata import data

print('all : \n ',data)
print('3 largest : ',heapq.nlargest(3,data))
print('3 smallesest : ',heapq.nsmallest(3,data))

print('Sorted : ',sorted(data)[:3])
