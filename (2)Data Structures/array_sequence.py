import array
import pprint

a = array.array('i',range(3))
print('Intial: ',a)

a.extend(range(3))
print('Extended: ',a)

print('Slice :',a[2:5])

print('Iterator:')
print(list(enumerate(a)))
