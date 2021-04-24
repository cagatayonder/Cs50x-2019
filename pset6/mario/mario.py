from cs50 import get_int 
while True:
    height = (get_int("Height(1-8): "))
    
    if 0 < height <= 8 :
        break    
        
for h in range(height):
    
    for i in range(height):
        
        if(i + h < height - 1):
            
            print(" ", end = "")
            
        else:
            
            print("#", end = "")
    print("  ", end = "")
    
    
    for k in range(height):
        
        if (k <= h):
            
            print("#", end = "")
        
    print()

