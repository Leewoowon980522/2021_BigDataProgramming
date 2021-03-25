#논리연산자
print(2<3)
print(3.14>100)
print("ABC"<="abc")
print("Lee">="lee")
print(3==1+2)
print(123=='123')
print(5!=5)
print('HELLO' != 'hello')
print("==========")
print(not False)
print(not 1)
print(not "")
print(not "Hello")
print(3<4 and 'a' != 'b')
print(3.14>5.5 and 'a'<='b')
print(3<4 or 'a'>'b')
print(3.14>5.5 or 'a' == 'b')
#연산자 우선순위
#낮은 순위의 연산을 먼저 실행하여면 소괄호로 둘러쌈
print(2+3*4)#14
print((2+3)*4)#20
print(9-5+2**2*1.5)#10.0
print(((9-5)+2)**(2*1.5))#216.0