class CalcFour:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        return result

    def sub(self):
        result = self.num1 - self.num2
        return result

    def mul(self):
        result = self.num1 * self.num2
        return result

    def div(self):
        result = self.num1 / self.num2
        return result


A = CalcFour(4, 10)

print(A.mul())


class MoreCalc (CalcFour):
    def pow(self):
        result = self.num1**self.num2
        return result


B = MoreCalc(4, 3)


print(B.pow())
print(B.mul())
