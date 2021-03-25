# List 생성
index = [1,2,3,4,5] # 숫자 List
indexs = ['a','b','c'] # 문자 List
listInlist = [1,2,3,['a','b','c'],4,5] # List속에 List
print(index),print(indexs),print(listInlist)

# List index값 가져오기
print(index[0]),print(index[1]),print(index[2])
#출력결과 : 1 2 3

# List index 음수로 표현
print(index[-1]),print(index[-2]),print(index[-3])
#출력결과 : 5 4 3

# List 내의 하나의 항목 접근
print(listInlist[3][0])#a

# List 내의 여러개의 항목 접근
print(index[0:3:1])#[1,2,3]
print(index[-3:0:-1])#[3,2]

#List 정렬(sort)
index1 = [5,4,87,1,3,4,9]
print(index1[:])#[5,4,87,1,3,4,9]
index1.sort()
print(index1[:])#[1,3,4,4,5,9,87]

#List 역순배치(reverse)
index1.reverse()
print(index1[:])#[87,9,5,4,4,3,1]

#List 특정항목 세기
findCountList = index1.count(4)
print(findCountList)#2 <- 4가 2개있기 때문
findCountZero = index1.count(100)
print(findCountZero)#0 <- 값이 없기 때문

#List 길이 구하기
lenIndex = [1,2,3,4,5,[1,2,3]]
nullIndex = []#항목X
print(len(lenIndex))#6
print(len(nullIndex))#0