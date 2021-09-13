
# coding: utf-8

# In[ ]:


myvar = 0
def notice(name):
    '''전달 받은 문자열을 포함하여 안내 메세지를 출력합니다.'''
    print("반갑습니다", name,"님")

def myfunc(a,b):
    '''두 개의 수치를 전달 받아서 사칙연산 결과를 리턴합니다.
    파라미터는 둘 다 산술 연산이 가능한 수치여야 합니다.'''
    return (a + b, a - b, a * b, a / b)

if __name__ == "__main__" :
    print("이 문자열을 출력합니다.")
    print(myfunc(10,5))
   