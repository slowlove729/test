# a 부터 b 까지의 정수의 합 구하기 for 문

print("a 부터 b 까지의 정수의 합을 구합니다.")

a = int(input("a 를 입력하세요 : "))
b = int(input("b 를 입력하세요 : "))


# a 와 b 정렬

if a > b:
    a, b = b, a

sum = 0


for i in range(a, b+1):
    sum += i

print(f"{a} 부터 {b} 까지의 정수의 합은 {sum} 입니다.")
