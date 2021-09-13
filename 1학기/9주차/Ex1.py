a = 0
b = {1,2,3}

while a<3:
    print("a가 3보다 작은 동안 출력")
    if a>1:
        if type(b) == set:
            if "1" in b:
                print("a가 1보다 크고 b가 집합이며 문자열 \"1\"이 b에 있는 경우 출력")
            else:
                print("a가 1보다 크고 b가 집합이며 문자열 \"1\"이 b에 없는 경우 출력")
    a += 1
print("while 종료,다음줄 실행")
print(a)