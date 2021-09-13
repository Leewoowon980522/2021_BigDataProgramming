#튜플 만들기
t1 = (1, 2, 3, 4, 5)
t2 = 1, 2, 3, 4, 5
t3 = (1,)# 항목이 하나인 튜플
t4 = ()# 항목이 없는 튜플
t5 = tuple()# 항목이 없는 튜플
print(t1,",",t2,",",t3,",",t4,",",t5)

#튜플내 1개의 항목 접근
print(t1[0],"===",t1[-1])

#튜플내 여러개의 항목 접근
print(t1[:3],",",t1[-1:2:-1])

#튜플에 대한 연산
a=(1,2,3)
b=(1,3,5)
print("덧셈 = ",a+b)
print("덧셈2 = ",a+(6,7,8))
#print(a+b[0]) #Error
print("덧셈3 = ",a+b[0:1])
print("곱셈 = ",2*a)

#튜플에 대한 크기비교
print((1,2,3,4,5)<(100,))
print((2,3,4) != "2,3,4")
print((1,2,3)[-1]==1)
#print((1,3,5)>=[0,1,2])#Tuple과 List라 Error

#튜플에 특정 값이 존재하는지 확인
tuple = (1,2,3)
print(1 in tuple)
print(5 not in tuple)

#튜플의 길이 구하기
tupleLen = (1,2,3)
len = len(tupleLen)
print(len)

#튜플에 있는 항목들의 합계,최대값,최소값 구하기
ex = (1,2,3,4,5,6,7,8,9)
sum = sum(ex)
max = max(ex)
min = min(ex)
print("sum = ",sum,", max = ",max,", min = ",min)

#튜플의 자료형 확인
types = (1,"Hi",3.14,True)
print("int = ",type(types[0]),", str = ",type(types[1]),", float = ",type(types[2]),", bool = ",type(types[3]),", tuple = ",type(types))

#튜플을 이용한 변수 할당
ch1 = 1
ch2 = 3.14
change1 = (ch1,ch2)
print(change1)
ch1,ch2 = ch2,ch1
print(ch1)
print(ch2)

#튜플 형태로 나눗셈의 몫과 나머지 구하기
dvm = divmod(7,3)
print(dvm)#(2,1)

#자료형 변환
#a = [1]
#b=tuple(a)
#c = [1,2,["hi","bye"],3,True]
#d=tuple(c)
#print(b)#(1,)
#print(d)#(1,2,['hi','bye'],3,True)
#a = (1,)
#b = (1,2,["hi","bye"],True)
#c = list(a)
#d = list(b)
#print(c)#[1]
#print(d)#[1, 2, ['hi', 'bye'], True]
