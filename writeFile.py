with open("test.txt", "r") as file:
    lines = file.readlines()
print("original file content:")
print(lines)
print("Reversed file content using lines[::-1]:")
print(lines[::-1])
print("Reversed file content using reversed(lines):")
with open("test.txt", "w") as file:
    for line in reversed(lines):
        print(line)
        file.write(line)
