mylist = [1,2,3]
def test1(t):
    return t.pop();

print("mylist = ",mylist)#mylist =  [1, 2, 3]
mypop=test1(mylist)
print("pop한 값=",mypop)#pop한 값= 3
print("mylist = ",mylist)#mylist =  [1, 2]
##################################################
dict = {"name":"이름","age":24}
def test2(d,name):
    d["name"]=name
    return d

print("old=",dict)#old= {'name': '이름', 'age': 24}

newDict = test2(dict,"이름2")
print("new=",newDict)#new= {'name': '이름2', 'age': 24}
print("old=",dict)#new= {'name': '이름2', 'age': 24}
##################################################
list1=[1,2,3]
def test3(t):
    t1 = list(t)
    return t1.pop()

print("list=",list1)#list= [1, 2, 3]

pop1=test3(list1)
print("pop한 값=",pop1)#pop한 값= 3
print("list=",list1)#list= [1, 2, 3]
##################################################
oldD={"name":"이름","age":24}
def test4(dd,name):
    d1 = dict(dd)
    d1["name"]=name
    return d1

print("old=",oldD)#old= {'name': '이름', 'age': 24}
newD = test4(oldD,"이름2")
print("new=",newD)#new= {'name': '이름2', 'age': 24}
print("old=",oldD)#old= {'name': '이름', 'age': 24}