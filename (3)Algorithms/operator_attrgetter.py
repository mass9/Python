from operator import *

class MyObj:
    ''' Example class for attrgetter'''
    def __init__(self,arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)

l = [MyObj(i) for i in range(5)]
print('Objects :',l)

# Extract the 'arg' values fro each object

g = attrgetter('arg')
vals = [g(i) for i in l]
print('arg values',vals)

#Sort using arg.

l.reverse()
print('reversed:',l)

