print("using readline =>")

try:
    with open("test.txt", "r") as file:
        while True:
            line = file.readline()
            if line=="":
                print("End of file reached")
                break
            print(line, end="")
except FileNotFoundError:
    print("File not found")
except Exception as ex:
    print(f"Exception raised: {ex}")

print("*"*50)
print("Pythonic way =>")
try:
    with open("test.txt", "r") as file:
        for line in file:
            print(line, end="")
    print("End of file reached")
except FileNotFoundError:
    print("File not found")
except Exception as ex:
    print(f"Exception raised: {ex}")
