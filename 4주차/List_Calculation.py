index = [1,2,3]
indexs = [4,5,6]
indexss = [4,6,5]
#List + 연산
print(index+indexs)#[1,2,3,4,5,6]
print(index+indexs[0:1])#[1,2,3,4]

#List * 연산
print(2*index)#[1,2,3,1,2,3]

#List 크기비교
print(index<indexs)#True
print(indexs>indexss)#False

#List에 있는 항목들의 합계 구하기
sum = sum(index)
print(sum)#[1,2,3] = 6

#List에 최대값 구하기
#strNum = [1,2,3,"A","B"]
max = max(index)
print(max)#3
#Error
#err = max(strNum)
#print("err",err)

#List에 최소값 구하기
min = min(index)
print(min)#1

#List에 자료형 확인(type)
typeIndex = [1,3.14,'Hi',True]
list = type(typeIndex)
num = type(typeIndex[0])
fnum = type(typeIndex[1])
str = type(typeIndex[2])
boolNum = type(typeIndex[3])
print("list :",list,"int :",num,"float :",fnum,"String :",str,"bool :",boolNum)

#List의 결합
exList1 = [1,2,3]
exList2 = [4,5,6]
exList1.extend(exList2)
print(exList1)#[1,2,3,4,5,6]
exList1.extend(["A","B"])
print(exList1)
#Error List가 아니기 때문
# exList1.extend("A","B")
# print(exList1)