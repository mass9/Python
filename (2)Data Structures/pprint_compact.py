from pprint import pprint

from pprint_data import data

print('DEFAULT:')
pprint(data,compact =False)
print('COMPACT:')
pprint(data,compact = True)
