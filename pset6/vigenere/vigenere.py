from sys import argv
from cs50 import get_string
import sys

if len(argv) != 2:
    exit("Usage: python vigenere.py key(str)")
    
if argv[1].isalpha() != True :
    exit("Usage: python vigenere.py key(str)")
    
argv[1].upper
    
key = []
i = 0
while i < len(argv[1]):
    
    key.append(argv[1][i].lower())
    i += 1
    
plaintext = get_string("plaintext: ")

j = 0
h = 0
print("ciphertext: ", end = "")

while j < len(plaintext):
    
    if not plaintext[j].isalpha():
    
        print(plaintext[j], end = "")
    
    if  plaintext[j].islower():
            
        print(chr((((ord(plaintext[j]) - 97 + (ord(key[h % len(key)].lower()) - 97))) % 26) + 97), end = "") 
        h += 1
    
    elif plaintext[j].isupper():
        
        print(chr((((ord(plaintext[j]) - 65 + (ord(key[h % len(key)].upper()) - 65))) % 26) + 65), end = "")
        h += 1
    
        
    j += 1

print()