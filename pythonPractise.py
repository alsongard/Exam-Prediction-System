for number in range(10):
    print(number)

print("\n")
for number in range(3,10):
    print(number)

print("\n")

#printing the array
a_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(a_list)
print(f"The type is {type(a_list)}")

print("\n")

# using only for item to get data
for item in a_list:
    print(f"data is {item} and the type is {type(item)}.")

print("\n")

#another method for iterating a list using while  statement
i = 0
while  i < len(a_list):
    print(f"the index value is {i} and the value of a_list is {a_list[i]}")
    i = i + 1

print("\n")

#using the for and range() to get index and  value
for number in range(len(a_list)):
    print(f"the value at index {number} is {a_list[number]}")

print("\n")
#using the enumareate 
for indexValue,item in enumerate(a_list):
    print(f"Index value : {indexValue} & Value is {item}.")

