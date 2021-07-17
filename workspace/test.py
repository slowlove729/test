# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c#problem

# x = test case number
# k = 행렬의 대각의 합
# r = 반복 되는 요소를 포함하는 행렬의 행 수
# c = 반복 되는 요소를 포함하는 행렬의 열 수

# testcase
x = int(input())


for i in range(x):
    matrix = []

    repeat = int(input())
    for j in range(repeat):
        line = input()
        number = line.split(" ")
        matrix.append([])
        for num in number:
            matrix[j].append(int(num))

    # print(matrix)
    k = 0
    r = 0
    c = 0
    for i in range(repeat):
        k += matrix[i][i]
        print(k)
