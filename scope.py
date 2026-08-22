# SCOPE determines the point at which you can access a variable.

# LEGB Rule
# Local scope - Variables defined inside functions.
# Enclosing scope - Variables defined in enclosing or nested functions
# Global scope - Variables defined at the toip level of a file
# Built-in scope - Names that Python provides. (print, str, type, isinstance)

# Example of local scope:
def my_func():
  my_var = 10      # This is the local scope this is the only place this variable is visible at.
  print(my_var)    # To make my_var a non-local variable use the 'nonlocal' keyword.

my_func()  # print 10 
# print(my_var) -> running this here will return a NameError

# Example of enclosing scope:
def outer_func():
    msg = 'Hello there!'

    def inner_func():   # This function can see within the scope of the outer function.
        print(msg)      # If a variable was declared here it cannot be seen by the outer function.

    inner_func()

outer_func() # Hello there!

# A solution will be to initialize the variable in the outer function so it can be modified
# by the inner function.

# Example of Global scope
# Variables declared outside any function, they can be acccessed from anywhere in the program.
my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100

# if you want to make a locally scoped vasriable defined inside a function globally accessible
# use the global keyword

my_var_1 = 7

def show_vars():
    global my_var_2      # Like this, you can also use this to modify an already global 
    my_var_2 = 10        # variable that resides outside a function.
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10

# Example of built-in scope
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False

