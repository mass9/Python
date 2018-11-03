import weakref

class ExpensiveObject:

    def __del__(self):
        print("Deleting {}".format(self))
def on_finalize(*args):
    print('on_finialize{!r}'.format(args))

obj=ExpensiveObject()
weakref.finalize(obj,on_finalize, 'extra argument')

del obj
