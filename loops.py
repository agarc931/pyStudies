# How to use loops

# Loops are used to repeat a block of code. In this lesson, 
# you will learn how to work with different types of loops in Python.

# the for loop
programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages: # will iterate through each index in the list 
    print(language)                    # and print it.

# Rust
# Java
# Python
# C++

# can also use a for loop through the string code and print out each character:

for char in 'code':
    print(char)

# c
# o
# d
# e

# you can nest for loops in python:

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for cartegory in categories:
    for food in foods:
        print(cartegory, food)

# the outer loop will iterate through each category in the categories list.
# for each category, the inner loop will iterate through each food in the foods list.
# Here is the result:
# Fruit Apple
# Fruit Carrot
# Fruit Banana
# Vegetable Apple
# Vegetable Carrot
# Vegetable Banana

# The while loop will repeat a block of code until thge condition is False
secret_number = 3
guess = 0

while guess != secret_number:                         # While the guessed number is not equal to the secret number
    guess = int(input('Guess the number (1-5): '))    # Get input from the user and assign it to the guess
    if guess != secret_number:                        # If the guess is not the secret number keep going
        print('Wrong! Try again.')

print('You got it!')                                  # Once the number inputted matches the secret number

# Python supports the 'break' and 'continue' statements
# here's an example of 'break'
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break                         # if the name is equal to naomi then we break out of the loop.
    print(developer)                  # output: Jess


# Here's an example of 'continue'
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue                       # If the name is equal to naomi then the iteration is skipped.
    print(developer)                   # output: Jess 
                                       #         Tom

# Both for and while loops can be combined with an else clause, executed only when the loop is not
# terminated by a 'break' statement. 
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")

# In this example we have a list of random words, and a for loop is used to loop through each word. 
# Inside the outer for loop, we have another for loop to loop through each letter of each word. 
# If the lowercase version of the letter is a vowel, we print the word followed by what vowels it contains, 
# then break out of the inner loop. If the word contains no vowels, then we print a message indicating that.

# OUTPUT
# 'sky' has no vowels
# 'apple' contains the vowel 'a'
# 'rhythm' has no vowels
# 'fly' has no vowels
# 'orange' contains the vowel 'o'

# notice how it breaks the second it hits the first vowel it doesn't count the rest.