# 반복을 통해 타입이 int형인 값만 출력
t = (1,"python",3.14,-999,False)
for i in t:
    if type(i) == int: #타입이 int형인것만 if구문 실행
        print(i)#1 -999

# s의 문자열출력 공백은 출력하지 않는다
s = "Hello, my name us 'Lee, W W'"
for c in s:
    if c != " ":
        print(c, end=" ")#print 마지막 부분에 end="원하는 문자열"을 사용하면 줄바꿈을 하지 않고 " "안에있는 문자열을 출력한다
#출력결과 : H e l l o , m y n a m e u s ' L e e , W W '