# To define functions use def and name it
# adding a () and a coilon : at the end will declare a function

# Name the function
def hello():
  # Add steps
  print('Hello World')  # The indentation will let python know that these 
                        # are the steps included in the function.
                        # This is a code block

hello()   # This is how to execute the function just created.

# Name a second function

def calculate_sum(a, b):  # You can declare they need input here like this.
  return a + b

calculate_sum(3, 1) # Should print 4
# If you call the function without the correct number of arguments
# you get a TypeError

#Functions also use a special return keyword to exit the function
#and return a value. Otherwise, they will return None by default

my_sum = calculate_sum(3, 1)
print(my_sum) #Will print None

# To fix this, we replace the print statement in the function 
# with a return statement. such as return a + b
