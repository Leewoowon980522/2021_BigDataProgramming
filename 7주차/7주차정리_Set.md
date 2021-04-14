# 7주차 정리
___
# Set(집합)
+ 순서가 없고 서로 다른 항목들이 모여있는 자료구조
+ 집합의 원소들은 모두 서로 다른 값으로서 동일한 값이 여러 개 존재할 수 없으며, 그들간 순서에 따른 구분이 없다
+ 원소들 간의 산술 연산이 정의되지 않는다

### 집합 만들기
+ 집합의 이름 = {값1,값2,...}
+ 괄호의 형태가 사전과 같으나 안에 들어가는 항목은 키-값의 쌍이 아닌 하나의 값
+ 자료 내에 중복값을 제거할땐 명령어 set을 사용하면 간단하게 처리가능하다
```python
    s1 = {1,2,3}
    s2 = {"a","b","c"}
    s3 = set([1,2,3,3,4])
    s4 = set("Hi")
    s5 = set()
    print(s1)#{1, 2, 3}
    print(s2)#{'b', 'c', 'a'}
    print(s3)#{1, 2, 3, 4}
    print(s4)#{'i', 'H'}
    print(s5)#set()
```
### 집합내 1개의 원소접근
+ 집합내 원소들은 순서가 존재하지 않아 인덱싱할수 없고, 사전처럼 키가 있는것도아니므로 리스트 또는 튜플로 변환한뒤 인덱싱함
```python
    getSet = {1,2,3}
    #print(getSet[0]) #TypeError: 'set' object is not subscriptable
    t1 = list(getSet)
    print(t1[0])# 1
```

### 집합에 1개의 원소 추가
+ 집합의 이름.add(새로운 원소)
```python
    addSet = {1,2,3}
    addSet.add(4)
    print(addSet)#{1, 2, 3, 4}
```

### 집합에 여러개의 원소 추가
+ 집합의 이름.update(1개의 리스트 or 튜플 or 문자열)
```python
    addSetUpdate = {1,2,3}
    addSetUpdate.update(["Add",4])
    print(addSetUpdate)#{1, 2, 3, 4, 'Add'}
```

### 집합내 원소 삭제
+ 집합의 이름.remove(삭제하려는 원소)
+ 존재 하지 않는 원소를 삭제 하려하면 오류가 발생
```python
    removeSet = {1,2,3,"Hi"}
    removeSet.remove("Hi")
    print(removeSet)#{1, 2, 3}
```

### 부분집합 확인
+ 집합의 이름.issubset(확인 하려는 다른 집합)
+ 대상 집합이 다른 집합의 부분 집합인지 검사하여 부분집합이면 True를 반환한다
```python
    a = {1,2,3}
    b = {1,2,3,4}
    c = {1,2}
    print(a.issubset(b))# True
    print(a.issubset(c))# False
    print(c.issubset(a))# True
```

### 상위집합 확인
+ 집합의 이름.issuperset(확인 하여는 다른 집합)
+ 대상 집합이 다른 집합의 상위 집합인지 검사하여 상위집합이면 True를 반환
```python
    a1 = {1,2,3}
    a2 = {1,2,3,4}
    a3 = {1,2}
    print(a2.issuperset(a1)) # True
    print(a1.issuperset(a3)) # True
    print(a3.issuperset(a1)) # False
```

### 집합내 특정 원소 존재확인
+ 찾으려는 원소 in 집합의 이름, 있다면 True반환
+ 찾으려는 원소 not in 집합의 이름, 없다면 True반환
```python
    findSet = {1,2,3}
    print(1 in findSet) # True
    print(4 in findSet) # False
    print(1 not in findSet) # False
    print(4 not in findSet) # True
```

### 교집합 구하기
+ 집합의 이름.intersection(다른 집합의 이름)
+ 집합의 이름 & 다른 집합의 이름
```python
    t1 = {1,2,3,4,5}
    t2 = {3,4,5,6,7}
    print(t1.intersection(t2))#{3, 4, 5}
    print(t1&t2)#{3, 4, 5}
```

### 합집합 구하기
+ 집합의 이름.union(다른 집합의 이름)
+ 집합의 이름|다른 집합의 이름
```python
    s1 = {1,2,3,4,5}
    s2 = {3,4,5,6,7}
    print(s1.union(s2))#{1, 2, 3, 4, 5, 6, 7}
    print(s1|s2)#{1, 2, 3, 4, 5, 6, 7}
```

### 차집합 구하기
+ 집합의 이름.difference(다른 집합이름)
+ 집합의 이름 - 다른 집합이름
```python
    m1 = {1,2,3,4,5}
    m2 = {3,4,5,6,7}
    print(m1.difference(m2))#{1, 2}
    print(m1-m2)#{1, 2}
```

### 집합의 크기 구하기
+ len(집합의 이름)
+ 원소의 개수를 리턴해준다
```python
    len1 = {1,2,3,4,5}
    len2 = {"Hi",1,2}
    l1 = len(len1)
    l2 = len(len2)
    print("len1 =",l1,"  len2 =",l2)#len1 = 5   len2 = 3
```

### 집합 자료형 확인
+ type(자료형을 확인할 1개의 자료)
+ 집합내 1개의 원소에 자료형을 확인하려면 자료형을 바꿔야함
```python
    type1 = {1,2,3}
    type2 = {"Hi","Bye"}
    type3 = {1.23,3.14}
    type4 = set()
    print("type1 =",type(type1))#type1 = <class 'set'>
    print("type2 =",type(type2))#type2 = <class 'set'>
    print("type3 =",type(type3))#type3 = <class 'set'>
    print("type4 =",type(type4))#type4 = <class 'set'>
    ch1 = list(type1)
    print(type(ch1[0]))#<class 'int'>
```