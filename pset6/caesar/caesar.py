from sys import argv
from cs50 import get_string

if len(argv) != 2:
    exit("Usage: python caesar.py n")

    
if argv[1].isdigit() != True:
    exit("Usage: python caesar.py n")

key = int(argv[1])
    
plaintext = get_string("plaintext: ")

i = 0

print("ciphertext: ", end = "")

while i < len(plaintext):
    
    if plaintext[i].isupper():
    
        print(chr(((ord(plaintext[i]) - 65 + key) % 26) + 65), end = "")
        
    elif plaintext[i].islower():
        
        print(chr(((ord(plaintext[i]) - 97 + key) % 26) + 97), end = "") 
        
    else:
        
        print(plaintext[i], end = "")
        
    i += 1
    
print()