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
