# If you place a string as the first thing in a function, without reference to a variable, it will be treated as a docstring.
# This is a docstring for the function in_fridge.
def  in_fridge(wanted_food):
    """Define a fridge with some food items."""
    fridge = {
        "misal": "He ahe misal hyala pava sobat khaa",
        "bhaji": "Hee ahe bhaji hila chapati sobat kha",
        "apple": "Haeahe fhal, hyala kha",
        "per": "Hae ahe dusra fhal hyala kha!"
    }
    try:
        count=fridge[wanted_food]
    except KeyError:
        count=0
    return count
print("%s"% in_fridge.__doc__)
# The docstring is referenced through a name that is part of the function, alomstw as though the function were a dictionary.
# The name is __doc__, and its found by following the function name wiht dot/period and the name __doc__.
# note that if you are using a name for a value in one function , that doesnt imply that is will creat ambiguity in the other function.
#  Which means that you can use the same name in different functions.
# Casue python provides a namespace for each function.
# Python have a scope for every varible,a dnit follows the vertical scale , where in the top most function is the global scope.
# The next function is the local scope.
# So if you have a variable in the global scope, it can be accessed by all the functions.
# Example:
special_sauce =["mayonnaise","ketchup","french dressing"]
def make_new_sauce():
        """This funciton makes a new special sauce."""
        special_sauce=["mustard","yogurt"]
        return special_sauce
print("%s"% special_sauce)
new_sauce=make_new_sauce()
# The function make_new_sauce() has a local variable special_sauce, which is different from the global variable special_sauce.
# So when you call the function make_new_sauce(), it will return the local variable special_sauce, which is different from the global variable special_sauce.
# So the global variable special_sauce will remain unchanged.
print("%s"% new_sauce)
 
def in_fridge(some_fridge, desired_item):
    """This is a functiontoseeif the fridge has a food. 
    fridge has to be a dictionary defined outside of the function. the food to be searched for is in the string wanted_food."""
    try:
        count =some_fridge[desired_item]
    except KeyError:
        count =0
    return count
fridge ={"apples":10,"bananas":5,"oranges":2}
wanted_food ="apples"
output=in_fridge(fridge,wanted_food)
print("The count of %s in the fridge is %d"%(wanted_food,output))
# The function in_fridge() takes two arguments, some_fridge and desired_item.
# some_fridge is a dictionary that is defined outside of the function, and desired_item is a string that is passed to the function.
# The function checks if the desired_item is in the some_fridge dictionary, and returns the count of the desired_item.
# If the desired_item is not in the some_fridge dictionary, it returns 0.
print(in_fridge({"cookies":10,"broocoli":3,"milk":2},"cookies"))
# just for instance consider that , if the user did not put any value for parameter in the function , in thise case
# the function will not work as expected, so we can provide a default value for the parameter.
def in_fridge(some_fridge, desired_item="milk"):
    """This is a function to see if the fridge has a food. 
    fridge has to be a dictionary defined outside of the function. the food to be searched for is in the string wanted_food."""
# here wehave created a defualt value by using the  assignment operator "="
# if you wirte a function with more than one parameter and you want to have both required and optional paramter , you have to place the optionals at the end of yourlist of parameters.
# This is because you have specified that a parameter is optinoal, it may or may not be ther.From the first optional laramtere , pyhton cannot gurantee the presence of the remaining parameters.
# That is every paramter after the first default parmeter becomes optional, this happens automatically.
#   Defining ja funcito within a function is called a nested function.Teh only care should be takne that the inner funcitn iw ate the same level of indentation as the rest of the code of the outer function.
def make_omlete(omlete_type):
    """This will make an omlete. You can either pass in a dictionary that conatins all of the ingredients for your omelete 
    ,or provide a tring to select a type  of omelete this functions already knows about.""" 
   
    def get_omlete_ingredients(omelete_name):
        """This contains a dictionary of omelete names that can be produced and their ingredients."""
        ingredients={"eggs":2,"milk":1,"salt":1,"pepper":1,"cheese":1}
        if omelete_name == "cheese":
            ingredients["cheese"] = 2
        elif omelete_name == "western":
            ingredients["jack_cheese"] = 3
            ingredients["ham"] = 1
            ingredients["pepper"] = 1
            ingredients["onion"] = 2

        elif omelete_name == "geek":
            ingredients["feta_cheese"] = 2
        else:
            raise TypeError("Unknown omelete type: %s"% omelete_name)
            
            
        return ingredients
    if type(omlete_type)==type({}):
        print("Omelete is a dictionary with ingredients")
        return make_food(omlete_type)
    elif type(omlete_type)==type(""):
        print("Omelete is a string with omelete name %s"% omlete_type)
        omlete_ingredients = get_omlete_ingredients(omlete_type)
        return make_food(omlete_ingredients, omlete_type)
def make_food(ingredeints_needed, food_name):
    """make(ingredeints_needed, food_name) takes the ingredients from the iningredients_needed and makes the food_name."""
    for ingredients in (ingredeints_needed.keys()):
        print("Adding %d to the %s to make %s omelete"%(ingredeints_needed[ingredients],ingredients,food_name))
    print("Your %s is ready!"% food_name)
    return food_name
# Here we have used the get_ingredients function inside the make_omelet function because . all the ingredients might differ according t9o the food one want to make.
# So we have used the get_ingredients function to get the ingredients for the food one want to make.
# The get_ingredients function is a nested function inside the make_omelet function.
print("Welcome to the Omlete maker! \n please select the type of omlete you want to make.")
options = ["cheese", "western", "geek"]
print("Available options are: %s"% options)
val= input(str("Enter the type of omlete you want to make: "))
omlete_type= make_omlete(val)
print(omlete_type)
# raise is another keyword for exception handling , it is the replacement of try and except.
# a good example to use a raise can be when you have written a function that accepts multiple parameteres and you have mentioned them all but one of them is of wrong type.
# when python calls a function in a main program of , function within a function , than it will create a list of all the calls , and this list i called stack.
# The stack is basically a list of all the function calls that have been made so far.
# When pyhton encounters a function call, it will stop its main program execution for a while , and note that where it has stopped. and this note is then stored in the stack.
# When the function call is completed, python will return to the main program and continue its execution from where it left off.
# The stack trace is a readable form of stack , which helps you to see exaclty where the problem happended.
varname='jagtap'
def another_varname():
    """Just checking the var name scope."""
    varname="sameer"
    print("The varname in the another_varname function is: %s"% varname)
print("The varname in the main program is: %s"% varname)
another_varname()
# The above code will print the varname in the main program and the varname in the another_varname function.
# The varname in the another_varname function is different from the varname in the main program.