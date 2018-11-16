import contextlib

class NonFatalError(Exception):
    pass
def non_idempotent_operation():
    raise NonFatalError('The operation faled because of existing state')

try:
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded 1')

except NonFatalError:
    pass

print('done')
