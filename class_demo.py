class Greeting:
    # Automatically called when we Create Object of Greeting Class 
    def __init__(self, message):
        print ("1. I am inside the Constructor")
        self.my_message = message
        

    def say_hello(self):
        print ("2. I am inside the say_Hello")
        print(self.my_message)

# Creating an object of the Greeting class

# object_name = classname
print ("0. About to Create the Instance of Class. i.e. Object")
greeting_object = Greeting("3. Ameet, Parse!")
print ("0.1. Constructor is called and about to call say_hello()")

# Calling the say_hello method
greeting_object.say_hello()
