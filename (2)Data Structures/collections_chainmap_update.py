

import collections

a = {'a':'A','b':'B', 'c':'D'}

b ={ 'd':'F', 'e':'Z'}

m = collections.ChainMap(a,b)

print('Before: {}'.format(m['c']))
a['c'] = 'E'

print('After:{}'.format(m['c']))

