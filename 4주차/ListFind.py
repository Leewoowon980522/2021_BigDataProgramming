#List의 특정값 찾기(True,False)
indexFind = [1, 2, 'Hello']
print(1 in indexFind)#True
print("Hello" in indexFind)#True
print("hello" in indexFind)#False, 대소문자를 구분
print('Hello' not in indexFind)  #찾는 값이 있으면 False,있으면 True반환