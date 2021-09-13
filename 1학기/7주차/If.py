# if1
if 3.14>2:
    print("True")
# 실행결과 True

# if - else
if 3.14<2:
    print("False")
else:
    print("True")

# elif
i = int(input("숫자입력:"))
if i>0:
    print("양수")
elif i<0:
    print("음수")
else:
    print("숫자0")

# 논리연산자 사용
num1 = 10
num2 = -5
if num1!=num2:
    print("같지않음")

# if문 중첩 사용
num = 100
if num>50:
    if num>100:
        print("num은 100보다 큽니다")
    else:
        print("num은 101보다 작습니다")