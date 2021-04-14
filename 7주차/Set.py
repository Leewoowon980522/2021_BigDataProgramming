# Set 생성
s1 = {1,2,3}
s2 = {"a","b","c"}
s3 = set([1,2,3,3,4])
s4 = set("Hi")
s5 = set()
print(s1)#{1, 2, 3}
print(s2)#{'b', 'c', 'a'}
print(s3)#{1, 2, 3, 4}
print(s4)#{'i', 'H'}
print(s5)#set()

# 집합내 1개의 원소접근
getSet = {1,2,3}
#print(getSet[0])#TypeError: 'set' object is not subscriptable
t1 = list(getSet)
print(t1[0])# 1

# 집합내 1개의 원소 추가
addSet = {1,2,3}
addSet.add(4)
print(addSet)#{1, 2, 3, 4}

# 집합에 여러개의 원소 추가
addSetUpdate = {1,2,3}
addSetUpdate.update(["Add",4])
print(addSetUpdate)#{1, 2, 3, 4, 'Add'}

# 집합내 원소 삭제
removeSet = {1,2,3,"Hi"}
removeSet.remove("Hi")
print(removeSet)#{1, 2, 3}

# 부분집합 확인
a = {1,2,3}
b = {1,2,3,4}
c = {1,2}
print(a.issubset(b))# True
print(a.issubset(c))# False
print(c.issubset(a))# True

# 상위집합 확인
a1 = {1,2,3}
a2 = {1,2,3,4}
a3 = {1,2}
print(a2.issuperset(a1)) # True
print(a1.issuperset(a3)) # True
print(a3.issuperset(a1)) # False

# 집합내 특정 원소 존재확인
findSet = {1,2,3}
print(1 in findSet) # True
print(4 in findSet) # False
print(1 not in findSet) # False
print(4 not in findSet) # True

# 교집합 구하기
t1 = {1,2,3,4,5}
t2 = {3,4,5,6,7}
print(t1.intersection(t2))#{3, 4, 5}
print(t1&t2)#{3, 4, 5}

# 합집합 구하기
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
print(s1.union(s2))#{1, 2, 3, 4, 5, 6, 7}
print(s1|s2)#{1, 2, 3, 4, 5, 6, 7}

# 차집합 구하기
m1 = {1,2,3,4,5}
m2 = {3,4,5,6,7}
print(m1.difference(m2))#{1, 2}
print(m1-m2)#{1, 2}

# 집합의 크기 구하기
len1 = {1,2,3,4,5}
len2 = {"Hi",1,2}
l1 = len(len1)
l2 = len(len2)
print("len1 =",l1,"  len2 =",l2)#len1 = 5   len2 = 3

# 집합 자료형 확인
type1 = {1,2,3}
type2 = {"Hi","Bye"}
type3 = {1.23,3.14}
type4 = set()
print("type1 =",type(type1))#type1 = <class 'set'>
print("type2 =",type(type2))#type2 = <class 'set'>
print("type3 =",type(type3))#type3 = <class 'set'>
print("type4 =",type(type4))#type4 = <class 'set'>
ch1 = list(type1)
print(type(ch1[0]))#<class 'int'>