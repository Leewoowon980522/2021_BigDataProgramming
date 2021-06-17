# Function(함수)

### 함수의 반환형태
+ 다음과 같은 경우 반환값이 없다
    + return 구문 자체를 사용하지 않을때
    + return 키워드만 기재했을떄
    + return None이라고 작성했을때
```python
def t1():
    print("테스트1")

def t2():
    print("테스트1")
    return
def t3():
    print("테스트1")
    return None
```
+ 그 외에는 함수의 반환 값이 존재하며, 반환되는 값은 언재나 1개이다
+ 반환된것은 지금까지 하던 작업을 마치고 자신을 호출한 곳으로 되돌아간다는 의미,여러개의 값을 하나씩 순서대로 반환할수없다
```python
def t4(a,b):
    print("a = ",a)#3
    print("b = ",b)#7
    return a+1
    return b+1

print(t4(3,7))#4

def t5(a,b):
    if a>b:
        return a+1
    else:
        return b+1
print(t5(3,7))#8
```
+ return 뒤에 여러개의 값을 기재하면, 그값들을 순서대로 항목을 가지는 튜플이 반환된다
```python
def t6(data):
    print("변수",data)#변수 [1, 3, 5]
    return sum(data),max(data),min(data)

sum_value,max_value,min_value=t6([1,3,5])
print("합계:",sum_value)#합계: 9
print("최대값:",max_value)#최대값: 5
print("최소값:",min_value)#최소값: 1
```
### 자료구조의 인자 전달
+ 변할수 있는 자료구조를 인자로 전달할때
    + 리스트,사전처럼 변할수있는 자료를 인자로 사용하면 함수 내에서 자료의 원본에 접근할수 있다.
```python
mylist = [1,2,3]
def test1(t):
    return t.pop();

print("mylist = ",mylist)#mylist =  [1, 2, 3]
mypop=test1(mylist)
print("pop한 값=",mypop)#pop한 값= 3
print("mylist = ",mylist)#mylist =  [1, 2]

dict = {"name":"이름","age":24}
def test2(d,name):
    d["name"]=name
    return d

print("old=",dict)#old= {'name': '이름', 'age': 24}

newDict = test2(dict,"이름2")
print("new=",newDict)#new= {'name': '이름2', 'age': 24}
print("old=",dict)#new= {'name': '이름2', 'age': 24}
```
+ 변할 수 있는 자료를 인자로 사용할 때는 그 자료가 수정 되는 경우에 대비하여 사본을 만들어 사용
```python
list1=[1,2,3]
def test3(t):
    t1 = list(t)
    return t1.pop()

print("list=",list1)#list= [1, 2, 3]

pop1=test3(list1)
print("pop한 값=",pop1)#pop한 값= 3
print("list=",list1)#list= [1, 2, 3]

oldD={"name":"이름","age":24}
def test4(dd,name):
    d1 = dict(dd)
    d1["name"]=name
    return d1

print("old=",oldD)#old= {'name': '이름', 'age': 24}
newD = test4(oldD,"이름2")
print("new=",newD)#new= {'name': '이름2', 'age': 24}
print("old=",oldD)#old= {'name': '이름', 'age': 24}
```

### 람다(Lambda) 함수
+ lambda 매개변수:표현식
+ 1개의 구문(표현식)으로 정의하는 축약된 형태의 함수
+ 기본적으로 이름 없이 사용될 수 있기 때문에 익명 함수 라고도 함
+ 매개변수를 받아서 표현식에 따라서 연산한 뒤 그 결과를 반환
+ 람다함수가 필요한 경우
  + 함수를 간단하게 한번만 사용하고 버릴 때
  + 다른 함수의 매개변수로 함수를 사용할 때
```python
f = lambda x:x+1
print(f(10))#11
print((lambda x,y:x*y)(2,3))#6

a=[1,2,3,"A"]
b=list(map(t1,a))
print(b)#[2, 4, 6, 'AA']

c=list(map(lambda x:2*x,a))
print(c)#[2, 4, 6, 'AA']
```