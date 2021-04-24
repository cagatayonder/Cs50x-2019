#include <cs50.h>
#include <stdio.h>

int main(void)
{   int height;
    do {
    height = get_int("height: ");
}
    while (height<1 || height>8);
int i,j;
for ( i = 0; i < height; i++) 
{for ( j = 0; j < height; j++) 
 { if (j + i < height - 1) 
     {printf(" "); }
      else 
         {  printf("#");  }           } 
         printf("  ");
         int k;
       {  for (k=0; k< height; k++ )
         { if (k<=i) 
    
         {  printf("#");  }}
    printf("\n");
}
}}
