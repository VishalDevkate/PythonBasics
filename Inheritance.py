from OOPsDemo import Calculator


class childCalculator(Calculator):
    num2 = 10

    def __init__(self, a, b):
        Calculator.__init__(self, a, b)
        print("child constructor executed")

    def add1(self, num1, num2):
        print("child add1 method called")
        print("self.num2 refers to parents num2") #6
        return self.num2 + num1 + num2

    def add2(self, num1, num2):
        print("child add2 method called")
        print("childCalculator.num2 refers to childs num2") #10
        return childCalculator.num2 + num1 + num2

if __name__ == "__main__":
    c1 = childCalculator(5,6)
    print(c1.add1(1, 2))
    print(c1.add2(1, 2))