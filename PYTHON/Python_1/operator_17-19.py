# 연산자

# 산술 연산자
# 더하기 +, 빼기 -, 곱하기 *, 나누기 /, 몫 //, 제곱 **, 나머지 %

# 관계 연산자
# 크다 > , 작다 < , 같다 == , 크거나 같다 >= , 작거나 같다 <= ,  같지않다 != 

print(1 != 1)
print(1 != 2)

print('-'*30)
# 논리 연산자
# and, or, not

a = True
b = False

print(a and b)
print(a&b) # & 와 and 는 같다, 둘 다 참이여야 참
print(a or b)
print(a|b) # | 와 or 은 같다, 둘 중 하나라도 참이면 참
print(a, not(a))
print(a is not b) #is 연산자는 동일 객체 비교 연산자 이다

print('-'*30)
# 할당 연산자
a = 100 # a 에 100을 할당 
print(a)
a+=1
print(a)
a-=1
print(a)
a*=2
print(a)
a/=2
print(a)

print('-'*30)
# 멤버쉽 연산자 

# in 연산자 
lst = [1,2,3,4,5]
print(lst, type(lst))

print(1 in lst)
print(6 in lst)

print('-'*30)
# bool 연산자 True(1), False(0)

print(bool(1))
print(bool(0))
print(bool(None)) # --> False
print(bool(-1)) # 음수도 True

