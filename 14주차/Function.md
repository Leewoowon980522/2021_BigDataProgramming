# Function(함수)
+ 입력값을 받아 일을 수행후 그 결과 값을 되돌려주는 구문들의 모음

### 함수사용 이유
+ 동일한 일을 수행하는 구문이 반복적으로 존재할 때
+ 프로그램의 흐름을 보다 구조적으로 만들기 위해

### 함수 호출
+ 결과 값을 할당할 변수 = 함수의 이름(필요한 입력값)
    + 존재하는 함수의 이름을 불러 그함수에게 담당한 일을 시키는것을 함수호출이라한다
```python
from builtins import type

a = type("3.141592")
print(a) # <class 'str'>
```
+ 함수들은 각자 역할의 따라 필요한 값의 종류와 개수가 다르고, 도출되는 결과의 종류가 다름
```python
a1 = 0
b1 = [1,2,3]
c1 = "Hello"
p1 = pow(3,4)
print(a1,b1,c1) # 0 [1, 2, 3] Hello
print(p1) # 81
```
+ 어떤 함수는 반드시 특정대상을 지정해야하고, 어떤 함수들은 범용적으로 사용할수있다, 이때 범용적으로 사용되는 함수를 내장함수라함
```python
a2 = len("Hello")
a3 = [1,2,3].pop()
print(a2) # 5
print(a3) # 3
```
### 기본적인 내장함수
+ print,input,len,pow,abs(절대값을 구하는함수),round
+ eval : 인자로 받은 문자열에 대하여 연산 또는 처리된 결과를 반환
+ sorted : 인자로 받은 자료구조의 항목들을 정렬된 리스트를 반환
+ range : x,y,z로 인자값을 받고 x~y전까지 간격 z단위로 나열된 정수의 목록을 반환
+ enumerate : 자료구조t,정수x 자료구조 t의 항목에 순서대로 정수 x부터 시작하는 번호를 부여한 튜플의 목록을 반환
+ zip : 각 자료구조 t1,t2에 동일한 위치의 항목들을 순서대로 묶은 튜플의 목록을 반환
```python
print(abs(1234))#1234
print(abs(-5.678))#5.678
print(round(3.9))#4
print(round(123.456,1))#123.5
print(round(123.456,-2))#100.0
a = eval("123+456")
b = eval(input("내용입력"))#내용입력3,9,-777,3.1425,123,1000
t = sorted(b)
print(a)#579
print(t)#[-777, 3, 3.1425, 9, 123, 1000]
a1 = (1,4,9,16)
b1 = list(enumerate(a1))
seasons = ["spring","summer","fall","winter"]
print(b1) #[(0, 1), (1, 4), (2, 9), (3, 16)]
for i,s in enumerate(seasons,1):
    print(s,i)
# spring 1
# summer 2
# fall 3
# winter 4
l1 = [1,2,3]
l2 = "abcd"
l3 = list(zip(l1,l2))
print(l3)#[(1, 'a'), (2, 'b'), (3, 'c')]
```
