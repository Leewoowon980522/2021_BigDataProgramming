# 대소문자 바꾸기
string1 = "aBcDeF"
print(string1.upper())#ABCDEF
print(string1.lower())#abcdef

#문자열 끝부분 문자 지우기
string2 = "!Hello world test!"
str1 = string2.lstrip("!")
str2 = string2.rstrip("!")
str3 = string2.strip("!")
print(str1)#Hello world test!
print(str2)#!Hello world test
print(str3)#Hello world test

#문자열 여러개의 문자열로 나누기
string3 = "Hello!World!Test!"
string4 = "Hello World Test!"
sp1 = string3.split("!")
sp2 = string4.split()
print(sp1)#['Hello', 'World', 'Test', '']
print(sp2)#['Hello', 'World', 'Test!']

#여러개의 자료 하나의 문자열로 결합
string4 = "Hello"
s1 = ",".join(string4)
s2 = " ".join(string4)
print(s1)#H,e,l,l,o
print(s2)#H e l l o