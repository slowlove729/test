# *을 n개를  w개마다 줄바꿈

n = int(input("* 을 출력할 개수를 입력 하세요 : "))
w = int(input("몇개 마다 줄바꿈 할까요 : "))

for i in range(1, n+1):
    print("*", end="")
    if i % w == 0:
        print("")

if n % w != 0:
    print("")
