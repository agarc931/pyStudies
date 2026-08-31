# What are ranges and how to use them
# range() - function is used to generate a sequence of integers.
#           range(start, stop, step)

# stop - integer that represents the end point for the sequence being generated.
#        this integer is not included.
print("with stop parameter: 3")
for num in range(3):
    print(num)

# OUTPUT: 0
#         1
#         2

# start - not required, default if not defined is 0 unles specified.
#         this integer is included.
print("with start and stop parameters: 1, 5")
for num in range(1, 5):
    print(num)

# OUTPUT: 1
#         2
#         3
#         4

# step - not required, default if not defined is 1 unless specified.
#        if you need to change the increment, specify one as a third parameter.
print(" with step parameter: 2")
for num in range(2, 11, 2):
    print(num)

# OUTPUT: 2
#         4
#         6
#         8
#         10

# If a stop argument is not specified you will get a TypeError
#  The stop parameter only takes integers, you'll get a TypeError by entering a float

# to generate a sequence of integers in decrementing order, then you can use a negative
# integer for the step argument
print("DECREMENTING!")
for num in range(40, 0, -10):
    print(num)

# a range object is immutable, which means it cannot be changed aftedr it is created. 
# a list is mutable, so you can change its values. 

# to generate a list of integers, pass a range to the list() constructor. 
print("making a list of integers")
numbers = list(range(2, 11, 2))
print(numbers)
# OUTPUT: [2, 4, 6, 8, 10]

