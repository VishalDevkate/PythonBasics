i = 10
while i > 0:
    print(i)
    i = i - 1

print("print till 6")
i =10
while i > 0:
    if i == 5:
        break
    print(i)
    i = i - 1

print("Skip printing 5 and print everything else")
i = 10
while i > 0:
    if i == 5:
        i = i - 1
        continue
    print(i)
    i = i - 1