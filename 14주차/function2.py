print(abs(1234))#1234
print(abs(-5.678))#5.678
print(round(3.9))#4
print(round(123.456,1))#123.5
print(round(123.456,-2))#100.0

a = eval("123+456")
#b = eval(input("내용입력"))#내용입력3,9,-777,3.1425,123,1000
#t = sorted(b)
print(a)#579
#print(t)#[-777, 3, 3.1425, 9, 123, 1000]

a1 = (1,4,9,16)
b1 = list(enumerate(a1))
seasons = ["spring","summer","fall","winter"]
print(b1) #[(0, 1), (1, 4), (2, 9), (3, 16)]
for i,s in enumerate(seasons,1):
    print(s,i)
# spring 1
# summer 2
# fall 3
# winter 4

l1 = [1,2,3]
l2 = "abcd"
l3 = list(zip(l1,l2))
print(l3)#[(1, 'a'), (2, 'b'), (3, 'c')]