from cs50 import get_string
from sys import argv


def main():

  if len(argv) != 2:
    exit("Usage: python bleep.py n")
  
    
  f = open(argv[1])
 
  banned_words = []
  
  for line in f:
      banned_words.append(line.rstrip("\n"))
  

  text1 = get_string("What message would you like to censor?\n")

  textlist1 = text1.split()
  
  
  for x in textlist1:
    if x.lower() in banned_words:
        i = 0
        
        while i < len(x) :
            
            print ("*" , end ="")
            i +=1
        print (" " , end="")     
    else :
            
            print (f"{x} ", end ="")
    
    

  print()

if __name__ == "__main__":
    main()
