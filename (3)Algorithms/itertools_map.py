# The built-in map() function returns an iterator that calls function on the values in the input iterators and return the result.

def times_two(s):
    return 2 *s

def multiply(x,y):
    return(x,y,x*y)

print('Doubles:')
for i in map(times_two,range(5)):
    print(i)

print('\n Multiples')
r1=range(5)
r2=range(5,10)
for i in map(multiply,r1,r2):
    print('{:d} * {:d} = {:d}'.format(*i))

print()
