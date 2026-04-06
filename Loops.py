list = [1,2,3,4,5]

total = 0
for i in list:
    print(i)
    total = total + i
print("total:",total)

print("using range")
for j in range(5):
    print(j)

print("define starting index")
for k in range(1,5):
    print(k)

print("using step value")
for a in range(1,10,2):
    print(a)
