# ENUMERATE AND ZIP FUNCTIONS
# enumerate() - Used to keep track of the index for an iterable and returns an enumerate object.
#               we put languages as a parameter into the enumerate object and the enumerate object
#               into the list object to concatenate a list with the attributes numbered.
languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# Each entry in the enumerate object (now a list) is a tuple containing a count, followed by a 
# value from the iterable passed to the enumerate() function.

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

