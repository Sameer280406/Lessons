# UNDERSTANDIG THE USE OF TRUE AND FALSE IN PYTHON 
# In python , basically when there is comparison with the double equals sign, there is a vlaue returned
# This vlaue is string that contains etiher true or false 
# when you compare two values like a list or a dictionary , there is a condition for which python will return the value as true
# And that is if each element is simliar to other and also there positions are equal/identical, which means python will still 
# return the value to be false if the elements are smae but are at different positions(I am here taking into consideration that 
# we are comparing lists and dictionaries)
# you can also compare with using <> this symbols to see which one is greater, also note that if you compare two strings 
# than python will go through each and every letter of the string to see which on is different and on the basis of that different letter
# it will compare the strigns and decide the output, truly automatic
print("Zebra">"Zebrb")
# here python went through every letter and found the difference at last in a,b where in it decided which one is greater
# While comparing the strings you might encoutner that you have two strings , one with uppper case letters and other with lowercase
# During this the comparison becomes difficult, you than cna use the .lowercase() method[will trun the string with all lowercase letters]
# and .uppercase() method [Will return the strings with all upper case methods]
print("Pumpkin"=="pumpkin")
print("Pumpkin".lower()=="pumpkin".lower())
str= "My name is Sameer Jagtap"
print(str.upper())
print(str.lower())
# for multiple objects you can use the and operation , where in it jsutifies like , if the operation on the left is ture then move one to the right and 
# evlaute the other one if both of them are true than the net value is true, if one of them is false , everything becomes false
# The excution begins from the leftmost.
# Using the if and else statement:
omlet_ingredients={"egg":2,"mushroom":5,"pepper":1,"cheese":1,"milk":1}
frigde_ingredients={"egg":10,"mushroom":20,"pepper":3,"cheese":2,"milk":15,"tomato":4}
have_ingredients=[False]
if frigde_ingredients["egg"]>omlet_ingredients["egg"]:
    have_ingredients[0]=True
have_ingredients.append("egg")
print(have_ingredients)
if frigde_ingredients["mushroom"]>omlet_ingredients["mushroom"]:
   if have_ingredients[0]==False:
       have_ingredients[0]=True   
have_ingredients.append("mushroom")
if frigde_ingredients["mushroom"]>omlet_ingredients["mushroom"]:
   if have_ingredients[0]==True:
       have_ingredients[0]=False   
have_ingredients.append("mushroom")
if frigde_ingredients["pepper"]>omlet_ingredients["pepper"]:
   if have_ingredients[0]==False:
       have_ingredients[0]=True   
have_ingredients.append("pepper")
if frigde_ingredients["cheese"]>omlet_ingredients["cheese"]:
   if have_ingredients[0]==False:
       have_ingredients[0]=True   
have_ingredients.append("cheese")
if frigde_ingredients["milk"]>omlet_ingredients["milk"]:
   if have_ingredients[0]==False:
       have_ingredients[0]=True  
have_ingredients.append("milk")
print(have_ingredients)
if have_ingredients[0]==True:
    print("I have ingredeints to make an omelet")
# To avoid or replace multiple if you can also use elif, only the change is that , the elif is executed only if the if statement is false
#  and in case of using multiple if's , all the if... statements will be executed
# Syntax of for loop , for i in range(start,stop,step):/code/, for while loop, while cond1:/code/
# to exit any loop you can use the "break" statement, the break statement will exit out of the most recent loop, like if a 
# while loop contains , a for loop in it , and this for loop have a break statement than , the loop exited will only be the for loop
# the while loop will continue without being affected by the break statement inside the for loop
# continueis a keyword that say to pyhton that , not to break the loop but instead skip to the rest of the program in the loop
# Example:-
for food in ("pate","cheese","rotten apples","crackers","whip cream","tomato soup"):
    if food[0:6] == "rotten":
        continue
    print("You can eat %s"% food)
# Here you can note that i have wrote food[0:6] which simply means that the starting six letters of the string in food must be equal to 
# rotten for the condition to be true
# Handling errors in python
# you can handle erroes using a try and except , where in the try block contains the code in which there is the possibility of erroe occuring 
# and the except blokc is responsible for handling the error, also a single try block can have multiple except blocks.
# for handling some error you can also make use of tuples in error handling 
# Examples:-
fridge_ingredients={"egg":8,"mushroom":20,"pepper":3,"cheese":2,"tomato":4,"milk":13}
try:
    if fridge_ingredients["orange juice"]>3:
        print("Sure, let's have some juice")
except(KeyError) as error:
    print("wooah , there is no %s"% error)
# Using tuple for multiple handling in one single except block
fridge_ingredients={"egg":8,"mushroom":20,"pepper":3,"cheese":2,"tomato":4,"milk":13}
try:
    if fridge_ingredients["orange juice"]>3:
        print("Sure, let's have some juice")
except(KeyError,TypeError) as error:
    print("wooah , there is no %s"% error)
# using the keyword "pass" to ignore certain exceptions, which are not neededliy being attention to:- 
fridge_ingredients={"egg":8,"mushroom":20,"pepper":3,"cheese":2,"tomato":4,"milk":13}
try:
    if fridge_ingredients["orange juice"]>3:
        print("Sure, let's have some juice")
except(KeyError) as error:
    print("wooah , there is no %s"% error)
except(TypeError)as error:
    pass