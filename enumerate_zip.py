# ENUMERATE AND ZIP FUNCTIONS
# enumerate() - Used to keep track of the index for an iterable and returns an enumerate object.
#               we put languages as a parameter into the enumerate object and the enumerate object
#               into the list object to concatenate a list with the attributes numbered.
languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))
# OUTPUT:
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# Each entry in the enumerate object (now a list) is a tuple containing a count, followed by a 
# value from the iterable passed to the enumerate() function.
print("Using enumerate with default index:")
print()

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

# OUTPUT:
# Index 0 and language Spanish
# Index 1 and language English
# Index 2 and language Russian
# Index 3 and language Chinese

# We unpack the count and value for each tuple in the enumerate object into variables 
# named index and language, respectively.
# both those variables are used in an f-string that's printed to the console in each iteration of the loop.

# enumerates() takes an optional start argument to set the count to start anywhere other than 0
#     enumerates(list, #)  -->  syntax
print()
print("Using enumerate with index 1:")
print()
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')

# OUTPUT:
# Index 1 and language Spanish
# Index 2 and language English
# Index 3 and language Russian
# Index 4 and language Chinese

# zip() - iterates over multiple iterables in parallel.
#         combines lists into pairs of elements and returns an iterator of tuples.
developers = ['Naomi' , 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

list(zip(developers,ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]
print()
print("Using zip iterating over devs and ids:")
print()

# And here's an example of using the zip() function with a for loop to iterate over 
# developers and ids:
for name, dev_id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {dev_id}')

# In this example, zip() combines the two lists into pairs of elements and returns 
# an iterator of tuples. The for loop then unpacks each tuple into name and dev_id. 
# Finally, for each print statement, we are printing each name and dev_id from the 
# ids and developers lists respectively. Here is what the result looks like in the console:

# OUTPUT:
# Name: Naomi
# ID: 1
# Name: Dario
# ID: 2
# Name: Jessica
# ID: 3
# Name: Tom
# ID: 4