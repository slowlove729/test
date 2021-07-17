# 0부터 9까지 출력하는 for 반복문
# for i in range(0,10):
#     print(i)

# 0부터 9까지 출력하는 while 반복문
# i = 0
# while i<10:
#     print(i)
#     i+=1

# 0부터 9까지 아래와 같이 출력하기
# 0       1       2       3       4       5       6       7       8       9
# for i in range(10):
#     print(i,end="\t")

# 0부터 9까지 아래와 같이 출력하기
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# n = 0
# for i in range(10):
#     if n < 9:
#         print(i,end=", ")
#     else:
#         print(i)
#     n += 1


# for 반복문을 사용해서 4부터 21까지의 홀수들의 합을 구하는 코드를 구현 하시오
# sum = 0
# first = 4
# last = 21
# for i in range(first,last+1):
#     if i % 2 != 0:
#         sum += i
#     else:
#         continue
# print(sum)


# 1부터 100까지의 수에서 짝수들만 출력하는 코드를 구현 하시오 (1)

# for i in range(1,101):
#     if i % 2 == 0:
#         print(i, end=" ")


# 1부터 100까지의 수에서 짝수들만 출력하는 코드를 구현 하시오 (2)
# num = 1
# while num < 101:
#     if num % 2 == 0:
#         print(num, end=" ")
#     num += 1

# 1부터 100까지의 수에서 짝수들만 출력하는 코드를 구현 하시오 (3)
# for i in range(2,101,2):
#     print(i, end=" ")


# 반복문을 이용해서 구구단 전체 출력

# 세로로 출력
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} x {j} = {i*j}")
#     print()

# 가로로 출력
# for i in range(1,10):
#     for j in range(2,10):
#         print(f"{j} x {i} = {j*i}", end="\t")
#     print("")


# 리스트 요소 반복문 출력
zoo = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligater']

# for animal in zoo:
    # print(animal)
    
# for i in range(len(zoo)):
#     print(zoo[i])


# 리스트 요소를 거꾸로 출력 하기
for i in zoo[::-1]:
    print(i)