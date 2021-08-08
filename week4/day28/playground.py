def add(*args):
    sum = 0
    for n in args:
        sum +=n
    #print(sum)
    return sum
print(add(5,12,10,11,99,-1,-150))

def calculate(a,b=5, *args, **kwargs):
    print (a,b,args,kwargs)

calculate(1,2,3,5,x=10, y=20)





