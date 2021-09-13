d1 = {"name":"홍길동","birth":"1월1일"}
d2 = {2016:"원숭이",2017:"닭",2018:"개",2019:"돼지",2020:"쥐"}
d3 = {("홍길동","000000"):[1,2,3],("김철수","111111"):[4,5,6]}
d4 = {}
d5 = dict()

# 사전 생성
print(d1)#{'name': '홍길동', 'birth': '1월1일'}
print(d2)#{2016: '원숭이', 2017: '닭', 2018: '개', 2019: '돼지', 2020: '쥐'}
print(d3)#{('홍길동', '000000'): [1, 2, 3], ('김철수', '111111'): [4, 5, 6]}
print(d4)#빈 사전
print(d5)#빈 사전

# 사전 내의 1개의 값 접근
print(d1["name"])#홍길동
print(d2.get(2016))#원숭이

# 사전의 특정 값 수정
d1["name"] = "이름변경"
print(d1.get("name"))# 이름변경
print(d3)#{('홍길동', '000000'): [1, 2, 3], ('김철수', '111111'): [4, 5, 6]}
d3[("홍길동","000000")][-1] = 200
print(d3)#{('홍길동', '000000'): [1, 2, 200], ('김철수', '111111'): [4, 5, 6]}

# 사전에 새로운 항목 1개 추가
addD = {"num1":1}
print(addD)#{'num1': 1}
addD["num2"] = 2
print(addD)#{'num1': 1, 'num2': 2}
# 사전에 항목 삭제
print(addD)#{'num1': 1, 'num2': 2}
del addD["num2"]
print(addD)#{'num1': 1}

# 사전에서 키 모음 가져오기
k1 = d2.keys()
print(k1)#dict_keys([2016, 2017, 2018, 2019, 2020])

# 사전에서 값 모음 가져오기
v1 = d2.values()
print(v1)#dict_values(['원숭이', '닭', '개', '돼지', '쥐'])

# 사전에서 키-값의 쌍 모음 가져오기
i1 = d2.items()
print(i1)#dict_items([(2016, '원숭이'), (2017, '닭'), (2018, '개'), (2019, '돼지'), (2020, '쥐')])

# 사전에 특정 키가 존재하는지 확인
print(2016 in d2)#True
print(2015 in d2)#False
print(2015 not in d2)#True
print(2016 not in d2)#False

# 사전에 특정 값이 존재 하는지 확인
print("쥐" in d2.values())#True
print("범" in d2.values())#False
print("쥐" not in d2.values())#False
print("범" not in d2.values())#True

# 사전에 특정 키-값의 쌍이 존재하는지 확인
print((2020,"쥐") in d2.items())#True
print((2020,"범") in d2.items())#False
print((2020,"쥐") not in d2.items())#False
print((2020,"범") not in d2.items())#True

# 사전의 길이 구하기
print(len(d2))#5

# 사전의 자료형 확인
print(type(d2))#<class 'dict'>
print(type(d2[2016]))#<class 'str'>
print(type(d3))#<class 'dict'>
print(type(d3[("홍길동","000000")]))#<class 'list'>

# 명령어를 사용한 사전 생성
d1 = dict(name = "이름1",birth = "생일",job = "직업")
print(d1)#{'name': '이름1', 'birth': '생일', 'job': '직업'}
d2 = dict(Y2016 = "원숭이",Y2017 = "닭")
print(d2)#{'Y2016': '원숭이', 'Y2017': '닭'}
#d3 = dict(2016 = "원숭이",2017 = "닭")#SyntaxError
#print(d3)

# 항목이 튜플인 리스트를 사전 자료형으로 변환
name = "이름"
birth = "생일"
job = "직업"
t1 = "name",name
t2 = "birth",birth
t3 = "job",job

data = [t1,t2,t3]
print(data)#[('name', '이름'), ('birth', '생일'), ('job', '직업')]

d1_list = dict(data)
print(d1_list)#{'name': '이름', 'birth': '생일', 'job': '직업'}

# 사전에 다른 사전 결합
print(d1_list)#{'name': '이름', 'birth': '생일', 'job': '직업'}
d1_other = {"birth":"생일2","company":"직장","position":"계급"}
d1_list.update(d1_other)
print(d1_list)#{'name': '이름', 'birth': '생일2', 'job': '직업', 'company': '직장', 'position': '계급'}

# 사전 생성시 주의할 점
#d = {[1,2,3]:"one,two,three"}
#print(d)#TypeError: unhashable type: 'list'
#d = {"name":"이름1","name":"이름2","bitrh":"생일"}
#print(d)#{'name': '이름2', 'bitrh': '생일'}