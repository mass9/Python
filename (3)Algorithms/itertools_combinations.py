from itertools import*

def show(iterable):
    first = None
    for i,item in enumerate(iterable,1):
        if first!=item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item),end= ' ')
    print()

print('All combination:')
print('Pairs')
show(combinations('abcd',r=3))