# break Ex1
a = input("문자열을 입력 (종료하려면 exit) :")
while True:
    print("입력한 내용은 : ",a)
    if a=='quit':
        break
    a = input("문자열을 입력 (종료하려면 exit) :")
print("반복구문 종료")