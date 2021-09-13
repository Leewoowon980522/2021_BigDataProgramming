print("Hello")

string1 ="Hello"
print(string1)
string1 = "First " + string1[0:]
print(string1) # First Hello

# 항목접근
findString = "Hello!"
print(findString[0])#H
print(findString[0:2])#He

# max,min
string2 = "aBcDeFg"
if "a" in string2 :
    print("string2길이 : ",len(string2))
print("min = ",min(string2)) #min =  B
print("max = ",max(string2)) #max =  g

# format
string3 = "test{} test".format("Hello")
print(string3) #testHello test

test = 123
string4 = "Hello{test} world{0}".format(test,test=456)
print(string4) #Hello456 world123

# 자리수 지정
string5 = "Hello world{0:5}".format("test")
print(string5)#Hello worldtest 

# 문자열 정렬
string6 = "문자열 정렬 {0:>10} 중".format("테스트")
print(string6)#문자열 정렬        테스트 중
string7 = "문자열 정렬 {0:<10} 중".format("테스트")
print(string7)#문자열 정렬 테스트        중
string8 = "문자열 정렬 {0:^10} 중".format("테스트")
print(string8)#문자열 정렬    테스트     중

# 문자열 공백
num = "Test"
string9 = "왼쪽정렬 {0:!<10}!로 채운다".format("test")
print(string9)#왼쪽정렬 test!!!!!!!로 채운다
string10 = "오른쪽정렬 {a:a>10}!로 채운다".format(a=123)
print(string10)#오른쪽정렬 aaaaaaa123!로 채운다
string11 = "중앙정렬 {:=^10}!로 채운다".format(num)
print(string11)#중앙정렬 ===Test===!로 채운다

# 문자열 소수점 지정
string12 = "숫자{0:.4f} or {1:0.4f}".format(3.14545,5.4546)
print(string12)#숫자3.1454 or 5.4546
string13 = "숫자{:=<10.3f}".format(3.145131)
print(string13)#숫자3.145=====

# 문자열 특정 항목 개수세기
string14 = "1231148"
print(string14.count("1"))#3

# 문자열 특정 항목 찾기
string14 = "12321"
find = string14.find("1")
print(find)#0
print(string14.find("3"))#2

string15 = "12321"
finds = string15.index("4")# error
print(finds)
print(string15.index("3"))#2