'''
Count Lines in a File
Objective: Count and print the number of lines in a file.

Instructions:

Use the attached text file "file1.txt"

Write a Python script that opens the file, reads through it line by line, counts how many lines it has, and prints the total count.

Expected result:

Total number of lines: 5
'''

file = open('file1.txt', "r")
noOfLines = 0
while True:
    line = file.readline()
    if not line:
        break
    noOfLines += 1
print("Total number of lines:",noOfLines)
file.close()

print("Alternative soln:")
noOfLines = 0
with open("file1.txt") as file:
    while True:
        line = file.readline()
        if not  line:
            break
        noOfLines += 1
print("Total number of lines:",noOfLines)