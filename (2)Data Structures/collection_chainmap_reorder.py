import collections

a = {'a':'A','b':'B', 'c':'D'}

b ={ 'd':'F', 'e':'Z'}

m = collections.ChainMap(a,b)

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print('d = {}'.format(m['d']))
print('e = {}'.format(m['d']))

print('Items:')
for k,v in m.items():
    print('{}: {}'.format(k , v))
print()

print ('"d" in m: {}'.format(('d' in m)))

# Printing Mapping 
print(m.maps)

#Reverse the list
m.maps = list(reversed(m.maps))
print(m.maps)
~                                                                     
~                                                                     
~
