# What Are Some Common Methods for Tuples?

# count() - This methjod is used to determine how many times an item appears in a tuple.
#           you wiill pass the value of what you're looking for as a parameter see below.
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2
# If the specified item in the count() function is not present at all in the tuple, the return
# value is 0. If you leave the parameter empty it will return a TypeError.

# index() - Used to find the index where a particular item is present in a tuple.
programming_languages.index('Java') # 1
# if the item specified cannot be found it will return a ValueError

# you can also pass in optional start and stop index arguments. 
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5
# in this example, we are specifyin where to start searching for the string 'Python'
# by passing in the numbver 3 as the second argument, we are starting the search at
# index 3. Since python appears twice in the tuple, the index function will return
# index 5 instead of 2.

# you can also pass in an optional stop index. 
programming_languages.index('Python', 2, 5) # 2
# Now the result is index 2 because we are starting the search at index 2, and searching up to
# but not including, index 5.

# sorted() - can be used in any iterable data types including tuples. It will create a new list
#.           of sorted values. This differs from the sort() method which sorts elements of a list
#            in a list in place and does not return a new list. 
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]

# if you need to customize the sorting behavioor for an iterable, you can use the optional
# reverse and key arguments.
# Here is an example of using the 'key' argument to sort items in a tuple by length
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

# if you want to create a new list of values in reverse order, then you can use the 'reverse'
# argument like this:
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']

# Tuples are a common data type in Python. Understanding how to work with them, along with 
# some helpful methods and functions, will help you write more efficient code.