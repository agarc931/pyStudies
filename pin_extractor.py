# defining pin extractor function to take the given poems as parameters
def pin_extractor(poems):

    # we'll need to store the list of secret codes generated
    secret_codes = []

    # iterate through the list of poems
    for poem in poems:

        # each poem will generate a secret code that we'll save here
        secret_code = ''

        # each poem needs to be divided in lines
        lines = poem.split('\n')

        # for each iteration of the lines list, assign it a number
        for line_index, line in enumerate(lines):

            # split each line to generate a list of words.
            words = line.split()

            # determine if the list has enough words to assign it a number.
            if len(words) > line_index:

                # if the line has enough words, measure the length of the
                # nth word of the list and concatenate it to the secret code
                secret_code += str(len(words[line_index]))

            else:

                # if the line doesn't have enough words, concatenate a 0
                secret_code += '0'

        # When the inner loop is finished, append the generated code to the list
        # of secret codes.        
        secret_codes.append(secret_code)

    # when all the iterations are over, return the list of generated secret
    # codes.
    return secret_codes    


# given poems for testing
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'

poem3 = 'There\nonce\nwas\na\ndragon'


# testing the pin extractor function.
print(pin_extractor([poem,poem2,poem3]))
