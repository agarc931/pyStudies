# Creating a program called caesar cipher 
# This is an encryption method that shifts letters
# in the alphabet to encode messages

def caesar(text, shift, encrypt = True):

  # check that the parameters meet the needded requirements
  if not isinstance(shift, int):
    return 'Shift must be an integer value'
  if shift < 1 or shift > 25:
    return 'Shift must be an integer between 1 and 25.'

  #check if the text should not be encrypted
  if not encrypt:
        shift = - shift
    
  # define the letters to be use for encryption
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  
  # takes 2 strings of equal length and returns a translation table that
  # maps each character of the first string with the corresponding 
  # character of the second string.
  
  translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
  
  # Use the translation_table to encrypt the text below using the translate method.
  encrypted_text = text.translate(translation_table)
  return encrypted_text

# To encrypt text
def encrypt(text, shift):
    return caesar(text, shift)
  
# To decrypt text
def decrypt(text, shift):
    return caesar(text, shift, False)

# Testing
encrypted_text = encrypt('freeCodeCamp', 3)
decrypted_text = decrypt('Pbhentr vf sbhaq va hayvxryl cynprf.', 13)

print(encrypted_text) # will print iuhhFrghFdps
print(decrypted_text) # will print Courage is found in unlikely places.
