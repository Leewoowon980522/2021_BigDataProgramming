# 정수 1~5까지 출력
for a in [1,2,3,4,5]:
    print(a)

# 각튜플별 앞자리 출력
a = [(1,2),(3,4)]
for i,j in a:
    print(i)

# 튜플 a,b,c,d,e에 들어 있는 값을 순서대로 결합하여 문자열 s를 만들어 s를 출력
t = ("a","b","c","d","e")
s = ""
for c in t:
    s += c
else:
    print(s)
# 중첩 ex1
for i in range(2):
    print("i가 0부터 1까지인 동안 출력,지금 i는",i,"입니다")
    for j in range(3):
        print("\t그 상황에서 j가 0부터 2까지인 동안 출력. 지금 j는",j,"입니다")

# 중첩 ex2
primes = []
for i in range(2,11):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        primes.append(i)
print("2부터 10사이의 소수는",primes,"입니다")#2부터 10사이의 소수는 [2, 3, 5, 7] 입니다