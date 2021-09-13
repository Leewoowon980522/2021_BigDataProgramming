# range
for i in range(3):
    print(i)
# 0 1 2
print("=======")

for i in range(1,5):
    print(i)
# 1 2 3 4
print("=======")

for i in range(1,10,2):
    print(i)
# 1 3 5 7 9
print("=======")

for i in range(10,0,-1):
    print(i)
# 10 9 8 7 6 5 4 3 2 1
print("=======")

for i in range(0,-7,-3):
    print(i)
# 0 -3 -6

# list 변환
a = list(range(3))
b = list(range(1,5))
c = list(range(1,10,2))
d = list(range(10,0,-1))
print(a)#[0, 1, 2]
print(b)#[1, 2, 3, 4]
print(c)#[1, 3, 5, 7, 9]
print(d)#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]