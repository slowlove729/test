n = int(input("몇번 번갈아 출력 할까요 : "))

for i in range(n//2):
    print("+-", end="")

if n % 2 != 0:
    print("+", end="")

print()
