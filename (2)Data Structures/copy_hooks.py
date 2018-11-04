import copy
import functools

@functools.total_ordering

class Myclass:

    def __init__(self,name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self,other):
        return self.name > self.other

    def __copy__(self):
        print('__copy()__')
        return Myclass(self.name)

    def __deepcopy__(self,memo):
        print('__deepcopy__({})'.format(memo))
        return Myclass(copy.deepcopy(self.name , memo))

a = Myclass('a')
sc = copy.copy(a)
dc = copy.deepcopy(a)
