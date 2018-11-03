import gc
import weakref

class ExpensiveObject:
    def __del__(self):
        print('Deleting {}'.format(self))
def on_finalize(*args):
    print('On_finalize {!r}'.format(args))

obj = ExpensiveObject()
obj_id = id(obj)

f = weakref.finalize(obj,on_finalize,obj)
f.atexit= False

del obj

for o in gc.get_objects():
    if id(o) == obj_id:
        print('Fount unc0llected object at gc')
