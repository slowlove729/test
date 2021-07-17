print("세 정수를 입력 받아 최댓값 구하기")

a = int(input("정수 a의 값을 입력하세요 : "))
b = int(input("정수 b의 값을 입력하세요 : "))
c = int(input("정수 c의 값을 입력하세요 : "))

# 최대 값을 저장하는 변수 maximum
maximum = a

if b > maximum: maximum = b
if c > maximum: maximum = c 

print(f"최댓값은 {maximum} 입니다.")