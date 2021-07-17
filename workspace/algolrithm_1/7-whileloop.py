# 1 부터 n 까지의 정수의 합 구하기 while문

print("1 부터 n 까지의 정수의 합 구하기")

n = int(input("n 값을 입력하세요 : "))

sum = 0
i = 1

while i <= n:
    sum+=i
    i+=1

print(f"1 부터 {n} 까지의 합은 {sum} 입니다.")