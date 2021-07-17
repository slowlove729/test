print("+ - 기호를 반복 출력하는 프로그램")

for i in range(int(input("몇개를 출력 할까요 : "))):
    if i % 2 == 0:
        print("+", end="")
    else:
        print("-", end="")

print()
