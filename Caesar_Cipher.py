#Cipher Game
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(len(alphabet))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#The Encrypt function
def caesar(message,input,choice):
if (choice=="encode"):
    
    cipher_text=""
    for i in message:
        if i in alphabet:
            old_index=alphabet.index(i)
            new_index=old_index + input
        cipher_text+=alphabet[new_index]
    print(f"The encoded text {cipher_text}")

    decipher_text=""
    for i in message:
        if i in alphabet:
            old_index=alphabet.index(i)
            new_index=old_index - input
        decipher_text+=alphabet[new_index]
    print(f"The decoded text is {decipher_text}")


# 

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#Call the caesar function and pass in the user inputs. You should be able to test the code and encrypt a message. 
caesar(text,shift,direction)
