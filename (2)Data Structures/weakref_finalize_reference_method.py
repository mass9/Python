import gc
import weakref

class ExpensiveObject:
    def __del__(self):
        print('Deleting {}'.format(self))
        
    def do_finalize(self):
        print('Do_finalize ')

obj = ExpensiveObject()
obj_id = id(obj)

f = weakref.finalize(obj,obj.do_finalize)
f.atexit= False

del obj

for o in gc.get_objects():
    if id(o) == obj_id:
        print('Fount unc0llected object at gc')
