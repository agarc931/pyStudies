# List Comprehensions and Useful Functions

# We used to iterate through lists like this:
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# List comprehension allows you to create a new list in a single 
# line by combining a loop and condition directly within square brackets. 
# This makes the code shorter and often easier to read.

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

# the even_numbers list is created using a single line of code. 
# The list comprehension loops through numbers from 0 to 20, and includes 
# only those that are divisible by 2. This approach is more compact and eliminates 
# the need for a separate loop and conditional block.

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

# OUTPUT:
# [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

# Another way to create a list starting from an existing iterable is the filter() function. 
# Here is an example of creating a new list of just words longer than four characters:
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

# filter() - used to select elements from an iterable that meet a specific condition.
#            Accepts a function and an iterable for its arguments. 
# map() - takes an iterable and applies a function to each of its elements.
#         Accepts a function and an iterable.
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# sum() - Used to get the sum from an iterable like a list or tuple.
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50

# you can also pass an optional start argument
numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total) # 60

