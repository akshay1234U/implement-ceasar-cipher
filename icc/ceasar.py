def encrypt(text, shift):
    encrypted_text = ""
    
  
    for char in text:
   
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
     
        else:
            encrypted_text += char
            
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    
   
    for char in text:
      
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
      
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
       
        else:
            decrypted_text += char
            
    return decrypted_text


def main():
    print("Caesar Cipher Encryption/Decryption")
    
   
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
   
    choice = input("Type 'E' to encrypt or 'D' to decrypt: ").upper()
    
   
    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please type 'E' or 'D'.")

if __name__ == "__main__":
    main()
