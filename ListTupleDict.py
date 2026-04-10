#List
values = [2, "hi", 3.14, True]
print(values)

values.append(4)
print(values)

values[0] = 10
values[-1] = 20
print(values)

print(values[1:3])

values.insert(1,"Rahul")
print(values)

#Tuple
val = (1, 2, 3)

print(val[0])
print(val)

#val[1] = 7  #error

#dictionary
dict = {
    "a": 1,
    2: 3.14,
    3: "Rahul"
}

print(dict)

#print(dict[0]) #keyerror
print(dict['a'])
print(dict[2])

dict["d"] = 'Hello'

print(dict.keys())
print(dict.values())
