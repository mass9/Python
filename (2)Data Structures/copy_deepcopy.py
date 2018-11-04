import copy
import functools

@functools.total_ordering

class Myclass:

    def __init__(self,name):
        self.name = name

    def __eq__(self,other):
        return self.name == other.name
    
    def __gt__(self,other):
        return self.name > other.name

a = Myclass('a')
my_list = [a]
dup = copy.deepcopy(my_list)

print('my_list              : ',my_list)
print('dup                  : ',dup)
print('dup is my_list       : ', (dup is my_list))
print('dup == my_list       : ', (dup is my_list))
print('dup[0] is my_list[0] : ',(dup[0] is my_list[0]))
