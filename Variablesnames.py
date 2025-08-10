monern=100
mongot=monern
monern = monern+200
print(mongot)
print(monern)
# This is just simply copying of the data from one variable to another , but when in the secon operation we
# changed the valus of the first variable , but  the vlaue of the second variable is retained as it is.
# TUPLES are immutable, which means that once they are created, they cannot be changed.
First_tuple = (1,2,3,4,5)
print(First_tuple)
# another method is 
print("This is a numbered tuple %d %d %d %d"%(1,2,3,4))
# priting a  tuple's elements individually
print("the first element of the tuple is %d" % First_tuple[0])
print("the second element of the tuple is %d" % First_tuple[1])
print("the third element of the tuple is %d" % First_tuple[2])
print("the fourth element of the tuple is %d" % First_tuple[3])
print("the fifth element of the tuple is %d" % First_tuple[4])
# tuple keepos the track of the elements in it , you can see the length of the tuple using the len() function
print("the length of the tuple is %d" % len(First_tuple))
# you can also use the type() function to check the type of the tuple 
# one can have multiple tuples , that is one tuple in another tuple 
second_tuple = (First_tuple, "second element of second tuple")
print(second_tuple)
# now accessing the elements of the first tupleis just easy, you can do so by just adding one more index
print(second_tuple[1]) 
# this will give the second element of the second tuple, which is a string
print(second_tuple[0][0]," ",second_tuple[1])  # this will give the first element of the first tuple *and the second element of t he second tuple
single_tuple= (1,) # this is a single element tuple, note the comma at the end
print(single_tuple)
# The another squence of  data is lists, which are mutable, which means that they can be changed after they are created
First_list = [1, 2, 3, 4, 5]
print(First_list)
# printing the elements of the list
print("the first element of the list is %d" % First_list[0])
print("the second element of the list is %d" % First_list[1])
print("the third element of the list is %d" % First_list[2])
print("the fourth element of the list is %d" % First_list[3])
print("the fifth element of the list is %d" % First_list[4])
# you can also use the len() function to check the length of the list
print("the length of the list is %d" % len(First_list))
# Just like tuples in , when you try to access an element that is out of range , it will give the same error as in tuple but, instead of 
# "tuple index out of range" it will give "list index out of range"
# You can add the  elements to the list using the append() method
First_list.append(6)
print("the list after appending 6 is %s" % First_list)
# If you wish to add more than one element at a time, you can use the extend() method
First_list.extend([7, 8, 9])
print("the list after extending with [7, 8, 9] is %s" % First_list)
# DICTIONARIES are another type of data structure in Python, which are mutable and are used to store key-value pairs
First_dict = {"name": "John", "age": 30, "city": "New York"}
print(First_dict)
# printing the elements of the dictionary
print("the name is %s" % First_dict["name"])
print("the age is %d" % First_dict["age"])
print("the city is %s" % First_dict["city"])
# Note that you can access the elements of the dictionary using the keys, which are unique,
# You can have two kys pointing to the same value, but you cannot have two keys with the same name
menu2 ={"Breakfast":"apple","Breakfast":"banana","Lunch":"rice","Dinner":"fish"}
print(menu2.get("Breakfast")) # This will return the last value assigned to the key "Breakfast", which is "banana"
# The initial value of the key BreakFast is just simply replaced by python with the newly assinged value banana
# With python we can treat a string like a list of inndividual characters ,with the help of slicing one can slice a string
# and can also excess the individual characters of a string
last_names=["Kadam","Jagtap","Nalawade","Nikam","Wagh"]
print("%s"%last_names[0])
print("%s"%last_names[0][0])
print("%s"%last_names[1])
print("%s"%last_names[1][0])
# With the write use of slicing we can create a dictionery of last names , with the keys as the initial letters of the 
# last names , while the vlaue would be the last name itself
names=["kadam","kanole","kanwade","kurmi","kuskhe"]
by_name = {}
by_name["k"] = []
by_name["k"].extend(names)
print(by_name)
# There are certain built-ins in python that are the keywords of python like none, ture, false , where in the none keyowrd is used 
# when you wirte a function and it has nothing to retrun , at that time it returns none
# using python you can access the last element with the use of negative integers , like for example
print("%s" % (names[-1]))
# with this as you keep increasing the vlaue of the index that is from -1 to -2 -3 and so on the list will be printed in the reverse order
# Remember that when you slice a string, list, tuple , the sliced part is it self a string,list, tuple respectively.
# One can create a sliced tuple list or string with the help of [start:end] syntax where in you mention the start address of slicing in the start part and the end address 
# of slicing in the end section, example.
slice_me=("The","next","time","we","meet","i","will")
sliced_me=slice_me[3:7]
print(sliced_me)
# You can use the pop method to remove a certainn element from a list , this method takes input the number/the index of the element to be removed
pop_me=["hii","helllo","konichiwa","bonjour","como estas","namaskar"]
popped_me=pop_me.pop(0)
print("The popped element is %s"% popped_me)
print(popped_me)
# Set are similar to dictionaries in python, except that they onsist of only key with no associated values.
# Essentially they are the collections of data with no dupicates. Set coems with two forms , mutable and immutable, the mutable is scuh that you can add , remove the values in it
# and immutabl is that once you set the initial values you cannot change them
# In Python, there is no official multi-line comment syntax like /* ... */ in some other languages.
# However, you can use triple-quoted strings (''' ... ''' or """ ... """) as a workaround.
# These are technically multi-line strings, but if not assigned to a variable, they are ignored by the interpreter.

"""
This is a multi-line comment.
It can span several lines.
Useful for documentation or temporarily disabling code.
"""

# You can also use multiple single-line comments:
# This is line 1
# This is line 2
# This is line 3
print(pop_me)