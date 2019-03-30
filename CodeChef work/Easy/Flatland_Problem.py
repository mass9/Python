import math

def Filterit(n):
    frac , whole = math.modf(math.sqrt(n))
    b.append(whole)
    if frac == 0.0:
        pass
    else:
        new = n- whole*whole
        Filterit(new)
    result = len(b)
    return result 


while True :
    try:
        # TODO: write code...
        T= int(input())
        while T > 0:
            b=[]
            print(Filterit(int(input())))
            T-=1
    except EOFError:
        break
