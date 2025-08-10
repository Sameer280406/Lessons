# Each of the object has three components: 1.an identity, 2.a type, and 3.a value.
# The identity refers to the location of the object being held in memory.And therefore is unchangeable.
# type refers to what type of data and values it can have, the value meanwhile can be changed in an object.
# but only if it set as mutable type. if it is immutable then it cannot be changed.
# A class allows you to define and encapsulate a group of objects into one convenient space.
# object contains both data and functions that operate on that data.
# WITH THE HELP OF dir FUNCTION YOU CAN SEE EVERYTHING THAT IS IN THE OBJECT.
# the dir function returns a list of all the names available in the object it is examining in aplhabetical order.
#print(dir(list))
# When a function is built into a object, it is called a method of that object.
# You can delcare a class using the class keyword.
class Fridge:
    """The definition of the fridge class,this class implements a fridge where ingredients can be added and removed individually,or in groups."""
# Better to implement the camel case for the names of the classes.
# Creating the object of the class Frigde.
f = Fridge()
f.items={}
f.items["Dahi Papdi Chat"]=2
f.items["Vada pav"]=4
# The methods that an object makes avaiable for use are called its interface, because this methods are how the program outside
# of the object makes use of object.
print(f.items)#try it yourself..
# Example:-
class Fridge:
    """This class implements a fridge where ingredients can be added and removed individually, or in groups. the fridge will retain 
    a count of every ingredients added or removed and will raisean error if a sufficient quantity of an ingredient isnt present.
    Methods:
    has(food_name[,quantity])-checks if the string food_name is in the  fridge. Quantity will be sent to 1 if you dont specify a number.
    has_various(foods)-checks if enough of every food in the dictionary is in the fridge.
    add_one(food_name)- adds a single food_name to the fridge
    add_many(food_dict)-adds a whole dictionary filled with food
    get-one(food_name)-takes out a single food_name from the fridge
    get-many(food_dict)-takes out a whole dictionary worth of food.
    get_ingredients(food)- IF passed an object that has the_ingredients method, get many will invoke this to get the list of ingredients
    """
    def __init__(self,items={}):
        """optionally pass in an initial dictionoary of items"""
        if(type(items)!=type({})):
            raise TypeError("Fridge requires a dictionary but was given a %s"%type(items))
        self.items=items
         # here ,when python creates an object , the __init__nethod is what passes the object its first parameter, the
    # self portion is actually a variable used to represent the instance of the object
        
    # In Python, classes are like blueprints for creating objects. When you define a class, you create both the "public"
    # parts (like the steering wheel and accelerator) that users of your class can directly interact with, and the "internal" 
    # or "private" methods (like the engine and transmission) that handle the inner workings of the class itself. 
    # These internal methods are functions defined within the class that are primarily meant for the class's own use, helping 
    # it manage its data and perform its specific tasks. They are not intended to be called directly from outside the class.
    """Single underscore prefix (e.g., _my_internal_method): This is the most common convention. It signals that the method is 
    intended for internal use within the class, but it can still be accessed (though it's generally discouraged) from outside. Think of it as a "protected" method.
    Double underscore prefix (e.g., __my_more_private_method): This triggers a mechanism called "name mangling". Python automatically renames these methods internally
    by adding the class name, making them harder to access directly from outside the class. This offers a stronger indication that the method is truly meant to be private to the class itself. """
        
       # the docstring and the intervening portion of the class would be here and
    # __add_multi should go afterwards
    def __add_multi(self, food_name, quantity):
        """This add multi adds more than one of a food item, returns the number of items added
        this should only be used internally, after the type checking has been done
        """
        if not food_name in self.items:
            self.items[food_name] = 0
        self.items[food_name] = self.items[food_name] + quantity

    def add_one(self, food_name):
        # adds a single food item in the dictionary
        if type(food_name) != type(""):
            raise TypeError("Add_one requires a string, given a %s type" % type(food_name))
        else:
            self.__add_multi(food_name, 1)

    def add_many(self, food_dic):
        # This function is responsible to add many food items at once 
        # basically it calls the add_multi function to add the many items in the fridge
        if type(food_dic) != type({}):
            raise TypeError("Add many requires a dictionary, and it actually got a %s type" % type(food_dic))
        else:
            for item in food_dic.keys():
                self.__add_multi(item, food_dic[item])
            return
    
    # add_one and add_many are there for similar purpose just to add the item in the fridge,and at the same time they both use 
    # _add_multi to actually do the heavy lifting.
    """With this you have a complete program that is capable of putting things  into the fridge but not taking them out of it 
    for that there will be further program"""
    # Demonstration
    """When you create an object from a class, self lets you access the data and methods that belong to that specific object."""
    def has(self,food_name,quantity=1):
        return self.has_various({food_name:quantity})

    def has_various(self,foods):
        """The has_various determines whether the dictionary food_name has enough of every element
        to statisy a request. and return true if there is enough , false if there is not or if element does 
        not exist"""
        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
            return True
        except KeyError:
            # print("There is an error named %s"%error) just if you want to print the error and don't forget to add the as error line in the except section
            return False
        # writing methdos to get the things out of the fridge
    def __get_multi(self,):
        
            
f = Fridge({"Eggs":30,"apples":40,"veggis":50})
print(f.items)
f.add_one("chaddi")
print(f.items)
f.add_many({"Baniyan":20,"Laptop":1,"lehenga":100})
print(f.items)
print(f.has("chaddi"))
if f.has("chaddi",1) and f.has("Baniyan",1):
    print("its time to wear a chaddi baniyan")
    
          