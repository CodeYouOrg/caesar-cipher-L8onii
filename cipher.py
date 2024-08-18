# Main Cipher Function with input text, -/+ # shift
def caesar_cipher_encrypt(text, shift):
    
    # Creates empty "encrypted text" list 
    encrypted_text = []

    # For loop for each character in input(text) 
    for char in text:

        # Checks to see if character is a alpha character 
        if char.isalpha(): 
            
            # Determine if the character is uppercase or lowercase and determines ord starting location (97 or 65)
            start = ord('A') if char.isupper() else ord('a')
            
            # Converts ord(#) to characters with shift within -/+ 26 character rotating range
            encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            
            # Adds each encrypted alpha character to encrypted list
            encrypted_text.append(encrypted_char)

        # Non alpha characters 
        else:

            # Adds each non-alpha character to encrypted list
            encrypted_text.append(char)

    # Attaches all characters together in a encrypted text
    return ''.join(encrypted_text)

def main():
    
    # Ask the user for input for text
    text = input("Message to encrypt: ")
    
    # Shifts either left or right depending on -/+ value
    shift = int(input("Enter shift amount '-/+ 1-26' :"))  
    
    # Text Shifted "-/+ 1-26" by previous shift amount requested above
    encrypted_text = caesar_cipher_encrypt(text, shift)

    # Prints encrypted message
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
# add your code here
