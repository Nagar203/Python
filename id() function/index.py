# id() function is a built-in function that returns the unique identifier of an object.

name = "string1"
duplicate_name = "string1" 
data1 = 10
data2 = 20
data3 = 10

data_list1 = [name, data1, data2, data3]
data_list2 = ["string1", 10, 20, 10]

print("Name: ", id(name))
print("duplicate_name: ", id(duplicate_name))

print("Data1: ", id(data1))
print("Data2: ", id(data2))
print("Data3: ", id(data3))

print("data_list1: ", id(data_list1))
print("data_list2: ", id(data_list2))

print("data_list1: ", id(data_list1[1]))
print("data_list2: ", id(data_list2[1]))