#include <stdio.h>
#include <cs50.h>
#include <math.h>
int main(void)
{
    float change;
    do{
        change = get_float("Para üstünü giriniz.\n");
    }while(change <= 0);
    int i = 0;
    int change1 = round(change*100);
    while(change1 > 0)
    {
      
        if(change1 >= 25)
        {change1 = change1 - 25;
        i++;}
        
        if(change1 >= 10 && change1 < 25){
        change1 = change1 - 10;
        i++;}
        
        if(change1 >= 5 && change1 < 10)
        {change1 = change1 - 5;
        i++;}
       
        if(change1 >= 1 && change1 < 5)
        {change1 = change1 - 1;
        i++;}
        
        
    }
   printf("%d\n", i);
    return 0;
}