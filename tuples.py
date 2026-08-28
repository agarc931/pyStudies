## WHAT ARE TUPLES ##
# A tuple is a Python data type used to create an ordered sequence of 
# values. Tuples can contain a mixed set of data types like this:
developer = ('Alice', 34, 'Rust Developer')
# I cannot assign a value directly to an index in a tuple. It will give me
# a type error.
# To access an index from a tuple you can call it the same way you can
# in a list.
developer[1] # 34
# If you need to access elements starting from the end of a tuple, 
# then you can use negative indexing.
numbers = (1,2,3,4,5)
developer[-2] # 4
# If you try to pass in an index number that exceeds or equals the length 
# of the tuple, then you will receive an IndexError

# To make a tuple out of  another variable use the tuple() method.
developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a')
# As a parameter you can pass in different iterable data types
# such as: strings, lists, and even other tuples.

# To check if an item is in a tuple, you can use the 'in' keyword like this:
programming_languages = ('Python', 'Java', 'C++', 'Rust')

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

# You can also unpack items from a tuple just like you did with lists:
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'
# In this example, name has the value 'Alice', age has the value 34, and job has the value 'Rust Developer'.
# If you need to collect any remaining elements from a tuple, you can use the asterisk (*) operator like this:
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

# Just like with a list, you can use the slice operator on a tuple to extract a portion of it. 
# Here is an example of extracting the items 'pie' and 'cookies' into a separate tuple:
desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3] # ('pie', 'cookies')
# Remember that the first number represents the starting index for the extraction while 
# the second number represents the ending index. But note that the item at the ending 
# index is not included in the extracted tuple.

# Since a tuple is immutable you cannot delete elements from a tuple like you can with a list.

# When might you use a tuple over a list?
# If you need a dynamic collection of elements where you can add, 
# remove and update elements, then you should use a list.
# If you know that you are working with a fixed and immutable collection of data, 
# then you should use a tuple.
