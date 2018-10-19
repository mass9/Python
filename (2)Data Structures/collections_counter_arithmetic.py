import collections

c1 = collections.Counter(['a','b','c','d','a','c','b'])
c2=collections.Counter('alpabet')

print('c1 :', c1)
print('c2 :', c2)

print('\nCombined counts')
print(c1 +c2)

print('\nSubtraction')
print(c1-c2)

print('\n Intersection ( Taking positive minimum ):')
print(c1 & c2)

print('\n Unions (taking maximums):')
print(c1 | c2)
