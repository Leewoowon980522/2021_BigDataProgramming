# 9주차 정리

# While

### 반복구문 - while
+ 조건문을 검사하여 결과가 참인 동안 while블록의 구문을 순서대로 반복실행
+ 조건문의 결과가 False가 되면 while문을 빠져나온다
```python
    while 조건 :
        조건이 참일때 실행 구문1
        조건이 참일때 실행 구문2
```
+ 정수 1~5까지 출력
```python
a = 1
while a<6:
    print(a)
    a += 1
```
### 반복구문 - while / else
+ 조건이 참이면 while아래 구문을 실행하지만 조건이 거짓이면 else아래 구문을 실행한다
```python
    while 조건 :
        참일경우 실행구문1
        참일경우 실행구문2
    else :
        거짓일경우 실행구문1
        거짓일경우 실행구문2
```
+ 정수를 입력받아 0이 아니면 입력한 정수출력 0이면 프로그램을 종료
```python
a = int(input("정수를 입력 : "))
while a != 0:
    print(a)
    a = int(input("정수를 입력 : "))
else:
    print("프로그램 종료")
```
### break
+ break는 자신이 속해있는 반복구문을 빠져나온다
+ 결과가 참이어도 break가 있으면 해당 반복구문은 종료된다
```python
# quit입력시 종료
a = input("문자열을 입력 (종료하려면 exit) :")
while True:
    print("입력한 내용은 : ",a)
    if a=='quit':
        break
    a = input("문자열을 입력 (종료하려면 exit) :")
print("반복구문 종료")
```
### continue
+ continue는 자신이 속한 반복구문의 맨 처음 위치로 돌아간다
```python
while True:
    a = int(input("양의 정수 입력 : "))
    if a<=0:
        continue
    print("입력한 값은 : ",a)
```