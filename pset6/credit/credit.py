from cs50 import get_int
import math


card_number = get_int("Credit card number: ")
    
n = 0
integars = []
    
while card_number >= 1:
    
    integar = card_number % 10
    
    card_number = math.floor(card_number / 10)
    
    n += 1
    
    integars.append(integar)
    
def luhn(integars):
    i = 1
    tf = []
    while i < len(integars):
    
        # sondan ikinci rakamların ikiyle çarpımlarının rakamlarının toplamı için
        t1 = integars[i] * 2
    
        if t1 >= 10:
    
            t1 = (t1 % 10) + 1
    
        tf.append(t1)
        i += 2
    
    tfinal = sum(tf)
    
    j = 0
    tl = []
    while j < len(integars):
    
        tl.append(integars[j])
        j += 2
    
    tfinal2 = sum(tl)
    tfinal3 = tfinal + tfinal2
    return tfinal3
    
check = [13, 15, 16]
    
if n not in check:
    
    print("INVALID")
    
if n == 13 or n == 16:
    
    if n == 16:
    
        if (integars[15] == 5) and (integars[14] == 1 or 2 or 3 or 4 or 5):
            
            if luhn(integars) % 10 == 0:
    
                print("MASTERCARD")
                
            else:
    
                print("INVALID")
                
        elif integars[15] == 4:
            
            if luhn(integars) % 10 == 0:
                
                print("VISA")
                
            else:
                
                print("INVALID")
                
        else:
            
            print("INVALID")
                
    if n == 13:
        
      {  if integars[12] == 4:
            
            if luhn(integars) % 10 == 0:
                
                print("VISA")
                
            else:
                
                print("INVALID")
    else:
        
         print("INVALID")
        }
if n == 15:
    
    if integars[14] == 3 and integars[13] == 4 or 7:
        
        if luhn(integars) % 10 == 0:
            
            print("AMEX")
            
        else:
            
            print("INVALID")
            
    else:
        
        print("INVALID")