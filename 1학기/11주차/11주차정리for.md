# 11주차 정리

# For

### 반복구문 - for
+ 변수에 들어갈 값이 없게되면 for문은 끝난다
+ in 뒤에 기재된 자료구조나 실행결과로부터 항목을 처음부터 끝까지 하나씩 꺼내어 변수에 넣어 for블럭의 구문들을 순서대로 반복한다
```python
    for 변수 in 반복 가능한 자료 또는 실행결과:
        변수에 값이 할당되는 동안 수행할 구문
```
+ 정수 1~5까지 출력
```python
for a in [1,2,3,4,5]:
    print(a)
```
+ 각 튜플별 앞자리 출력
```python
a = [(1,2),(3,4)]
for i,j in a:
    print(i)
```

### while과 for의 차이
+ while은 참/거짓으로 논리를 검사할때,for구문은 여러 차례 순서대로 내용을 추출할때 사용

### for/else문
+ 변수에 값이 할당되는 동안 for구문을 실행
+ 변수에 더이상 들어갈 값이 없으면 else문 실행
```python
for 변수 in 순회가능한 자료 또는 실행결과:
    변수에 값이 할당될때 실행구문
else:
    변수에 값이 할당되지 않을때 실행구문
```
+ 튜플 a,b,c,d,e에 들어 있는 값을 순서대로 결합하여 문자열 s를 만들어 s를 출력
```python
t = ("a","b","c","d","e")
s = ""
for c in t:
    s += c
else:
    print(s)
```
### break/continue
+ break
    + 자신이 속해있는 구문을 빠져나온다
    + 아직 변수에 할당할 값이 남아있어도 break를 만나면 반복구문은 종료된다
+ continue
    + 자신이 속해있는 반복 구문의 맨 처음 위치로 돌아간다
    + continue를 만나면 반복 구문의 맨 처음 위치로 돌아가 그 다음 값을 변수에 할당한다

### range
+ for구문과 함께 사용되는 범위 지정
+ for 변수 in range(시작위치,끝위치,간격)
```python
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
```
+ range의 결과 리스트로 만들기
    + list(range(시작위치,끝위치,간격))
    + range의 실행 결과인 정수의 목록은 그 자체가 리스트는 아니지만 리스트로 변환할 수 있다
    + 튜플, 집합도 가능하다
```python
a = list(range(3))
b = list(range(1,5))
c = list(range(1,10,2))
d = list(range(10,0,-1))
print(a)#[0, 1, 2]
print(b)#[1, 2, 3, 4]
print(c)#[1, 3, 5, 7, 9]
print(d)#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```
### 반복 구문 중첩
+ 구문은 필요에 따라 중첩할수 있다
+ 중첩된 하위블록은 상위 블록에 종속됨
```python
for i in range(2):
    print("i가 0부터 1까지인 동안 출력,지금 i는",i,"입니다")
    for j in range(3):
        print("\t그 상황에서 j가 0부터 2까지인 동안 출력. 지금 j는",j,"입니다")
```
```python
primes = []
for i in range(2,11):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        primes.append(i)
print("2부터 10사이의 소수는",primes,"입니다")#2부터 10사이의 소수는 [2, 3, 5, 7] 입니다
```
### 리스트 함축 기법
+ 리스트이름 = [연산 for 변수 in 기존자료 if 조건문]
    + if조건문은 생략 가능
+ for구문을 리스트 자료 구조의 내부에 직접 기재하여 새로운 리스트를 만든다
```python
a = [1,2,3]
b = [i*2 for i in a]
print(b)#[2, 4, 6]

c= [57,-9,3.14,0,-123.45]
d = [x for x in c if x>0]
print(d)#[57, 3.14]
```
### 사전 함축 기법
+ 사전이름 = {키:값 for 변수 in 기존자료 if 조건문}
    + if조건문은 생략 가능
```python
e = {"a":1,"b":2,"c":3}
f = {v:k for k,v in e.items()}
print(f)#{1: 'a', 2: 'b', 3: 'c'}

g = (1,2,3,4,5)
h = {x:x * 3 for x in g if x %2 ==1}
print(h)#{1: 3, 3: 9, 5: 15}
```