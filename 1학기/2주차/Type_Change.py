#자료 형변환
#int
print(int(3.14))
print(int(True))#1
print(int(False))#0
print(int("123"))#123
#print(int("Hi")) <- X 문자열은 숫자만 가능
#print(int("3.14")) <- "3.14"는 실수형도 아니고 정수만으로 이루어진 문자열이 아니기 때문에 오류가 발생한다.

#float
print(float(3))
print(float(False))
print(float(True))
print(float("1234"))
print(float("3.1415")) # 문자열이지만 실수 형태이기에 가능하다
#print(float("True")) <- 논리형이 아닌 문자열이기 때문에 오류가 발생한다.

#str
print(str(1))
print(str(3.14))
print(str(1.2e4))
print(str(True))
print(str(False))
print(str("문자열")) # 문자열은 그대로 출력된다.

#bool
print(bool(3))
print(bool(0))
print(bool(3.14))
print(bool(0.0))
print(bool("문자열"))
print(bool(""))
print(bool(True))
print(bool(False))