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
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')



