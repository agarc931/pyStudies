# Throughout the previous lessons, you have been used to defining functions
# by using the def keyword like this:
def square(num):
    return num ** 2

print(square(4)) # 16

# Lambda functions are anonymous inline functions. This function no longer has the name square 
# associated with it.
lambda num: num ** 2  # This is what the square() function would look like.

#  Lambda functions are great when you need to use them in higher order functions like this:
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
# In this example, we have a list of numbers and want to create a new list of even numbers. 
# So we pass in a lambda function as one of the arguments to the filter() function to get a new 
# list containing the numbers 2 and 4.

# Don't assign lambda functions to variables, this defeats the purpose
# of anonymous functions. If needed to save the function or make it reusable,
# use regular funcion.

# Avoid creating lambda functions that are difficult to read or 
# unnecessarily complicated. Like if it involves multiple steps

