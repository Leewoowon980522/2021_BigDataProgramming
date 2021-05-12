# 리스트 함축 기법
a = [1,2,3]
b = [i*2 for i in a]
print(b)#[2, 4, 6]

c = [57,-9,3.14,0,-123.45]
d = [x for x in c if x>0]
print(d)#[57, 3.14]

# 사전 함축 기법
e = {"a":1,"b":2,"c":3}
f = {v:k for k,v in e.items()}
print(f)#{1: 'a', 2: 'b', 3: 'c'}

g = (1,2,3,4,5)
h = {x:x * 3 for x in g if x %2 ==1}
print(h)#{1: 3, 3: 9, 5: 15}