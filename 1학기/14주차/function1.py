from builtins import type

a = type("3.141592")
print(a) # <class 'str'>

a1 = 0
b1 = [1,2,3]
c1 = "Hello"
p1 = pow(3,4)
print(a1,b1,c1) # 0 [1, 2, 3] Hello
print(p1) # 81

a2 = len("Hello")
a3 = [1,2,3].pop()
print(a2) # 5
print(a3) # 3