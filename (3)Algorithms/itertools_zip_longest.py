from itertools import *

r1= range(3)
r2= range(4,10)

print('zip stop early')
print(list(zip(r1,r2)))

r1= range(3)
r2= range(6,10)

print('\nzip longes processes all of the values:')
print(list(zip_longest(r1,r2)))

