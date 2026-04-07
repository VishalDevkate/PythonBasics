class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("Calculator constructor executed")

    def add(self, num1, num2):
        print("adding two numbers")
        print("addition of passed numbers: ", num1 + num2)
        return self.num1 + self.num2

    def subtract(self, num1, num2):
        return self.num1 - self.num2

if __name__ == "__main__":
    c1 = Calculator(1, 2)
    print(c1.add(3,4))