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
