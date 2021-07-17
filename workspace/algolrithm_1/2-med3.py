print("세 정수를 입력 받아 중앙값 구하기")

def med3(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a >= c:
            return c
        else:
            return a
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


print(f"med3(1,1,1) = {med3(1,1,1)}")
print(f"med3(1,1,2) = {med3(1,1,2)}")
print(f"med3(1,1,3) = {med3(1,1,3)}")
print(f"med3(1,2,1) = {med3(1,2,1)}")
print(f"med3(1,2,2) = {med3(1,2,2)}")
print(f"med3(1,2,3) = {med3(1,2,3)}")
print(f"med3(1,3,1) = {med3(1,3,1)}")
print(f"med3(1,3,2) = {med3(1,3,2)}")
print(f"med3(1,3,3) = {med3(1,3,3)}")
print(f"med3(2,1,1) = {med3(2,1,1)}")
print(f"med3(2,1,2) = {med3(2,1,2)}")
print(f"med3(2,1,3) = {med3(2,1,3)}")
print(f"med3(2,2,1) = {med3(2,2,1)}")
print(f"med3(2,2,2) = {med3(2,2,2)}")
print(f"med3(2,2,3) = {med3(2,2,3)}")
print(f"med3(2,3,1) = {med3(2,3,1)}")
print(f"med3(2,3,2) = {med3(2,3,2)}")
print(f"med3(2,3,3) = {med3(2,3,3)}")
print(f"med3(3,1,1) = {med3(3,1,1)}")
print(f"med3(3,1,2) = {med3(3,1,2)}")
print(f"med3(3,1,3) = {med3(3,1,3)}")
print(f"med3(3,2,1) = {med3(3,2,1)}")
print(f"med3(3,2,2) = {med3(3,2,2)}")
print(f"med3(3,2,3) = {med3(3,2,3)}")
print(f"med3(3,3,1) = {med3(3,3,1)}")
print(f"med3(3,3,2) = {med3(3,3,2)}")
print(f"med3(3,3,3) = {med3(3,3,3)}")