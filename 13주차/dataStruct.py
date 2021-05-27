# 동일 객체 비교 연산자
a = 123
b = 123
c = 1234
print(a == b)  # True
print(a is b)  # True
print(a == c)  # False
print(a is c)  # False
# 2개의 자료 동일 객체 검사 연산자
a1 = [1, 2, 3]
a2 = [1, 2, 3]
a3 = a1
print("a1 =",id(a1)," a2 =",id(a2))
print(a1 == a2)  # True
print(a1 is a2)  # False
print(a1 == a3)  # True
print(a1 is a3)  # True
