# 배열,리스트,자료형

# 아래 리스트 중에 korea, 365, 400 의 값이 출력되도록 작성하시오
# a = [100, 3.14, 'korea', [1,2,3,365], (100,200,300,400,500)]

# print(a[2])
# print(a[3][3])
# print(a[4][3])


# 역인덱스, 거꾸로, 리스트

# a = [100,200,300,400,500]
# print(a[::-1])


# 인덱스, 반복문, 리스트

# 아래와 같이 출력 하기
# 0 = 100         1 = 200         2 = 300         3 = 400         4 = 500         5 = [1, 2, 3]           6 = (4, 5, 6)

# a = [100,200,300,400,500,[1,2,3],(4,5,6)]

# for i in range(len(a)):
#     print(i,end=' = ')
#     print(a[i],end='\t\t')
# print()


# 리스트 오름차순 점수

# score = [ 100, 40, 70, 90, 60]

# 오름차순
# print(sorted(score))

# 내림차순
# print(sorted(score,reverse=True))

# score.sort(reverse=True)
# print(score)

# 정렬함수에는 sort(), sorted()가 있는데
# sort()는 list.sort(reverse=False) 처럼 사용하고 리스트 자체를 정렬하고
# sorted()는 NEW_LIST = sorted(list, reverse=True) 처럼 사용하고 새로운 리스트를 반환 한다.


# 역인덱스 출력
# a = [100, 40, 70, 90, 60, 25, 67, 45, 9, 5, 76, 21]

# a.sort(reverse=True)
# for i in range(-len(a), 0):
#     print(f"{a[i]} ( {i} )", end="\t")


# 리스트 추가 수정 삭제
# score = [90, 80, 70, 60, 50]
# print(score)
# score.append(40)  # 추가
# print(score)
# score.remove(70)  # 삭제
# print(score)
# score[1] = 100  # 변경
# print(score)
# score.pop()  # 마지막 요소 삭제
# print(score)
# del score[0]  # 인덱스 요소 삭제
# print(score)


# 리스트 병합
# a = [0, 1, 2, 3, 4]
# b = [5, 6, 7, 8, 9]

# ls = a + b
# print(ls)
# ls = a + a + a
# print(ls)
# ls = a * 3
# print(ls)


animals = ["elephant", "hippo", "lion", "tiger", "alligator"]
for animal in animals:
    print(animal, end="\t\t")
print()
user_input = input("케이지를 알고 싶은 동물의 이름을 입력하세요 = ")

animal_index = animals.index(user_input)
print(
    f"{user_input} 동물의 케이지는 {animal_index}번 위치에 있습니다. {animal_index}번 케이지 약도를 출력하시겠습니까?"
)

# match = False
# cnt = 0
# while match != True:
#     if animals[cnt] == user_input:
#         print(f"{user_input} 동물의 케이지는 {cnt}번 위치에 있습니다. {cnt}번 케이지 약도를 출력하시겠습니까?")
#         match = True
#     else:
#         cnt += 1
