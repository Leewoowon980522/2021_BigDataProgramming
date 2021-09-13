def t1():
    print("테스트1")

def t2():
    print("테스트1")
    return
def t3():
    print("테스트1")
    return None
def t4(a,b):
    print("a = ",a)#3
    print("b = ",b)#7
    return a+1
    return b+1
print(t4(3,7))#4

def t5(a,b):
    if a>b:
        return a+1
    else:
        return b+1
print(t5(3,7))#8

def t6(data):
    print("변수",data)#변수 [1, 3, 5]
    return sum(data),max(data),min(data)

sum_value,max_value,min_value=t6([1,3,5])
print("합계:",sum_value)#합계: 9
print("최대값:",max_value)#최대값: 5
print("최소값:",min_value)#최소값: 1