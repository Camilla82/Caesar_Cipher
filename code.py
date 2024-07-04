alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = "" # create a blank string to store the encrypted text 
    for letter in plain_text: # create a loop to iterate through each letter in the plain text
        position = alphabet.index(letter) # find the position of the letter in the alphabet list and store it
        new_position = position + shift_amount # create the new position by adding the shift amount to the current position
        new_letter = alphabet[new_position] # find the new letter by indexing the alphabet list with the new position
        cipher_text += new_letter # ad the new letter to the cipher text string 
        print(f"The encoded text is {cipher_text}") # print the encrypted text       
      
encrypt(plain_text= text, shift_amount= shift) # call function encrypt with the user inputs 

