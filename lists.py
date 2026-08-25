# list
cities = ['Los Angeles', 'London', 'Tokyo']

cities[0] # 'Los Angeles'

# Negative indexing is used to access elements starting from 
# the end of the list instead of the beginning
cities[-1] # 'Tokyo'

# The list() constructor is used to convert an iterable 
# into a list like this:
developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']

# An iterable is a special type of object that can be looped 
# over one item at a time. 

# To get the total number of elements in a list, you can use the 
# len() function like this:
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5

# If you wanted to update a value at a particular index, you can do something like this:
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

# If you pass in an index (either positive or negative) that is out of bounds 
# for the list, then you will receive an IndexError:

# If you want to remove an element from a list you can use the del keyword like this:
developer_list = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']

# Sometimes it is helpful to check if an element is inside the list. To do that, 
# you can use the in keyword like this:
'Rust' in programming_languages # True
'Python' in programming_languages # False

# Sometimes it is common to have lists nested inside of other lists like this:
developer_nested = ['Alice', 25, ['Python', 'Rust', 'C++']]

# To access the nested list, you will need to access it using index 2 
# since lists are zero based indexed:
developer[2] # ['Python', 'Rust', 'C++']

# Then to access the second language from that nested list,
# you will need to access it using index 1 like this:
developer[2][1] # 'Rust'

# Unpacking values from a list is a technique used to assign values from a list to 
# new variables. Here is an example of unpacking a developer list into 
# new variables called name, age and job.
name, age, job = developer_list

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

# If you need to collect any remaining elements from a list, 
# you can use the asterisk (*) operator like this:
name, *rest = developer_list

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

# If the numbers of variables on the left side of the assignment operator doesn't match the total 
# numbers of items in the list, then you will receive a ValueError

# The slice operator (:) Similar to strings, you can access portions of a list by using the slice
# operator like this:
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']
# the start index is 1 since that points to the second item in the list. 
# Then we use the slice operator followed by an end index of 4, which includes 
# everything up to (but not including), the item at that index.

# Another thing you can do with the slice operator : is specify a step 
# interval which determines how much to increment between the indices.
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]

# There are some common methods associated with lists such as:
# append(), extend(), insert()
# pop()
# sort()

# How to use append() -- This is used to add an item at the end of the list.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

# you can also use this method to add a list at the end of another.
even_numbers = [6, 8, 10]
numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, [6, 8, 10]]
# Notice how the even_numbers nested inside the numbers list.

