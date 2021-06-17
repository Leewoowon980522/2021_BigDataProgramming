f = lambda x:x+1
print(f(10))#11
print((lambda x,y:x*y)(2,3))#6

def t1(x):
    return 2*x
a=[1,2,3,"A"]
b=list(map(t1,a))
print(b)#[2, 4, 6, 'AA']

c=list(map(lambda x:2*x,a))
print(c)#[2, 4, 6, 'AA']