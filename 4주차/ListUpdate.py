#List에 값추가,수정,삭제
#List에 항목 추가(append)
index1 = [1,2,3]
index1.append(4)
print(index1[:])#4가 추가됨
#값추가
index1.append("Hello")
index1.append(True)
print(index1[:])#'Hello'와 True가 추가됨

#List에 특정위치에 항목추가(insert)
index2 = [1,2,3]
index2.insert(1,4)#2번째 항목에 4추가, 원래 2번째 부터 끝에 있는거 까진 하나씩 밀림
print(index2[:])#1,4,2,3
index2.insert(-2,10)
print(index2[:])#1,4,10,2,3

#List에 항목 삭제(del)
index3 = [1,2,3,4,5]
del index3[1]
print(index3[:])#[1,3,4,5]
del index3[1:]
print(index3[:])#[1]

#List에 항목 삭제(remove)
index4 = [1,2,3,4,5,2]
index4.remove(2)#정수형2를 삭제한다.
print(index4[:])#첫번째에 있는 2는 삭제되고 두번째 2는 삭제되지 않는다.

#List에 항목 삭제(pop)
index5 = [1,2,3,4,5]
deleteindex = index5.pop(2)
print("index :",index5[:],"deleteindex :",deleteindex)#index : [1,2,4,5] deleteindex : 3
index5.pop()#생략할경우 마지막 항목이 제거
print(index5[:])#마지막 5가 사라짐