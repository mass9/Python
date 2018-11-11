# The starmap() fuction is similar to map(), but instead of construction a tuples from multiple iterators , it splits up the items in single iterator

from itertools import *

values = [(0,5),(1,6),(2,7),(3,8),(4,9)]

for i in starmap(lambda x,y : (x,y,x*y),values):
    print('{} * {} = {}'.format(*i))
