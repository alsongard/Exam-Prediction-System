import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
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


#show an example of how to plot data
apple = [0.9, 1.3, 0.7, 0.8, 1.8]
year = list(range(2004,2009))
#range() lastValue - 1
plt.bar(year,apple)
plt.title("apple yearly production")
plt.xlabel("year")
plt.ylabel("apple production")
plt.show()

#enhance plotting by using sn (seaborn)
sn.set_style("darkgrid")
plt.bar(year, apple)
plt.title("apple yearly production")
plt.xlabel("year")
plt.ylabel("apple production")
plt.show()

#multiple data sets 
sexEducation = [1,7,4,5,8,9,1]
breathingSystem = [8,4,5,2,1,6,4]
year = list(range(2004,2011))
sn.set_style("darkgrid")
plt.bar(year, sexEducation)
plt.bar(year, breathingSystem, bottom=sexEducation)
plt.legend("sexEducation", "breathingSystem")
plt.title("Exam Data Capture")
plt.show()
#from the data collected above it seems it added the values of the topics in each year and present them
# these method is not preferrable for our system as we want to compare the occurences from the diffrerent topics