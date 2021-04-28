a = 3
while a:
    print("값이 ",a,"입니다")
    a -= 1
while False:
    print("while이 True일 경우 출력")
else:
    print("While이 False일 경우 출력")
while "False":
    print("while이 True일 경우 출력")
    break
else:
    print("While이 False일 경우 출력")