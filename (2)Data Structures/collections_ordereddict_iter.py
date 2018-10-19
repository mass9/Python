import collections
print('Regular dictionary:')
d = {}
d['c'] = 'C'
d['b'] = 'B'
d['a'] = 'A'

for k,v in d.items():
    print(k,v)

print('\nOrderedDict:')
d= collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k,v in d.items():
    print(k,v)
