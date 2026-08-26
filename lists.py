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
# del developer_list[1] if this line was added, it would
# return an error when called this list below
print(developer_list) 

# Sometimes it is helpful to check if an element is inside the list. To do that, 
# you can use the in keyword like this:
'Rust' in programming_languages # True
'Python' in programming_languages # False

# Sometimes it is common to have lists nested inside of other lists like this:
developer_nested = ['Alice', 25, ['Python', 'Rust', 'C++']]

# To access the nested list, you will need to access it using index 2 
# since lists are zero based indexed:
developer_nested[2] # ['Python', 'Rust', 'C++']

# Then to access the second language from that nested list,
# you will need to access it using index 1 like this:
developer_nested[2][1] # 'Rust'

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

### METHODS ###  
#There are some common methods associated with lists such as:
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

# But if you want to add all of the individual numbers from the even_numbers list at the end 
# of the numbers list, then you can use the extend() method. Similar to append() but you
# can add multiple elements from one list to another
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

# To insert an element at a specific index in a list, you can use the insert() method. 
# This method accepts two arguments: the index where you wish to insert the new 
# item and the item you want to insert.
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]
# This inserted the 2.5 in index 2, and shifted the rest of the element by one position.

# To remove an element from a list, you can use the remove() method. It takes the value
# of the element to remove as an argument
numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50]
# As you can see, it only removes the FIRST occurrence in the list.

# To remove an element at a specific index in the list, you can use the 
# pop() method like this:
numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned
# If you don't specify an element for the pop methif, the last element is removed.
numbers = [1, 2, 3, 4, 5]
numbers.pop() # The number 5 is returned

# To empty the list, you can use the clear() method like this:
numbers = [1,2,3,4,5]
numbers.clear()

print(numbers)  #[]

# The sort() method is used to sort the elements in place.
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]

# sorted() works for any iterable and returns a new sorted list instead of modifying
# the original list.
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]
# an iterable is a special type of object that you can loop over, allowing you to access each item one at a time.

# reverse() will reverse a list of elements in place like this:
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]

# index() is used to find the first index where an element can be found in a list.
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1
# if the element cannot be found, then Python throws a ValueError
