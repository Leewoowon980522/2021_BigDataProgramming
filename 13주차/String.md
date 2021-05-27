# 13주차 정리

# 문자열

### 문자열(String)
+ 문자,단어등으로 이루어진 문자들의 집합
+ 따옴표로 둘러싸여있는것
```python
print("Hello")
```
+ 튜플처럼 문자열 내의 문자를 수정/삭제할수 없고 추가할수도 없다
+ 수정하려면 인덱싱,슬라이싱 및 덧셈등을 사용해 할당한다
```python
string1 ="Hello"
print(string1)
string1 = "First " + string1[0:]
print(string1) # First Hello
```

### 문자열
+ 1개의 항목 접근/여러개의 항목 접근
    + 리스트나 튜플과 동일한 방식으로 인덱싱
```python
findString = "Hello!"
print(findString[0])#H
print(findString[0:2])#He
```
+ 문자열 특정값 존재확인
    + in,not in
+ 문자열 길이 구하기
    + len
+ 문자열 최대값,최소값구하기
    + max,min
```python
# max,min
string2 = "aBcDeFg"
if "a" in string2 :
    print("string2길이 : ",len(string2))
print("min = ",min(string2)) #min =  B
print("max = ",max(string2)) #max =  g
```
+ 문자열 포맷 지정
  + 서식포함 문자열.format(서식에 넣을 내용)
  + 문자열 내에 {}가 있으면 {}안에 내용이 들어가짐
```python
string3 = "test{} test".format("Hello")
print(string3)#testHello test

test = 123
string4 = "Hello{test} world{0}".format(test,test=456)
print(string4) #Hello456 world123
```
+ 문자열 자리수 지정
```python
string5 = "Hello world{0:5}".format("test")
print(string5)#Hello worldtest 
```
+ 문자열 정렬
```python
string6 = "문자열 정렬 {0:>10} 중".format("테스트")
print(string6)#문자열 정렬        테스트 중
string7 = "문자열 정렬 {0:<10} 중".format("테스트")
print(string7)#문자열 정렬 테스트        중
string8 = "문자열 정렬 {0:^10} 중".format("테스트")
print(string8)#문자열 정렬    테스트     중
```
+ 문자열 공백 채우기
```python
num = "Test"
string9 = "왼쪽정렬 {0:!<10}!로 채운다".format("test")
print(string9)#왼쪽정렬 test!!!!!!!로 채운다
string10 = "오른쪽정렬 {a:a>10}!로 채운다".format(a=123)
print(string10)#오른쪽정렬 aaaaaaa123!로 채운다
string11 = "중앙정렬 {:=^10}!로 채운다".format(num)
print(string11)#중앙정렬 ===Test===!로 채운다
```
+ 문자열 소수점 자리수 지정
```python
string12 = "숫자{0:.4f} or {1:0.4f}".format(3.14545,5.4546)
print(string12)#숫자3.1454 or 5.4546
string13 = "숫자{:=<10.3f}".format(3.145131)
print(string13)#숫자3.145=====
```
+ 문자열 특정 항목 개수 세기
```python
string14 = "1231148"
print(string14.count("1"))#3
```
+ 문자열 특정 항목 찾기
  + find
    + 문자열에서 처음으로 나오는 위치를 돌려줌,존재하지 않을시 -1반환
  + index
    + 문자열에서 처음으로 나오는 위치를 돌려줌,존재하지 않을시 오류 반환    
```python
string14 = "12321"
find = string14.find("1")
print(find)#0
print(string14.find("3"))#2

finds = string15.index("4")# error
print(finds)
print(string15.index("3"))#2
```
