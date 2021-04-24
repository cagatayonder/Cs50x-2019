from cs50 import get_float

while True:
    
    money = get_float("Para Üstü: ")
    
    if money > 0:
        break
money = round(money * 100)
count = 0
    
while money > 0:
    
    if money >= 25:
        
        money -= 25
        count += 1
        
    elif money >= 10 and money < 25:
        
        money -= 10
        count += 1
        
    elif money >= 5 and money < 10:
        
        money -= 5
        count += 1
        
    else:
        
        money -= 1
        count += 1
        
print(count)