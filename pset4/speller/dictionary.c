#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"


#define N 26


typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;



node *hashtable[N];

unsigned int word_count= 0;
unsigned int head;


unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}


bool load(const char *dictionary)
{
    // Hash tablosunu başlatır
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }
   

    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

  
    char word[LENGTH + 1];

   // Dosya sonu olmayan dizeleri tarar
    while (fscanf(file, "%s", word) != EOF)
    {
        // Yeni düğüm için bellek ayırma
        node *new_node = malloc(sizeof(node));
// Eğer malloc NULL ise, return false
        if (new_node == NULL)
        {
            return false;
        }
// Sonraki düğüme işaretçi ve kelimenin kendisi
        strcpy(new_node->word, word);
        // head elde etmek için elde kelimeyi hash hale getirin
        head = hash(word);
        // Yeni işaretçi ayarla
        new_node->next = hashtable[head];
        // head'i yeni işaretçiye ayarla
        hashtable[head] = new_node;
        // Kelime sayısını artır
        word_count++;
    }


    // Sözlüğü kapa
    fclose(file);

    // Indicate success
    return true;
}

// Eğer sözlüğe yükleme başarılı ise kelime sayısını verir, değilse 0 döner
unsigned int size(void)
{
    if (word_count > 0)
    {
        // yüklenen kelime sayısını verir
        return word_count;
    }
    return 0;
}

// Kelime sözlükte ise doğru, aksi takdirde yanlış döndürür
bool check(const char *word)
{
    //head için kelimeyi hashler
    head = hash(word);
    //bağlantılı listeye eriş
    node *cursor = hashtable[head];
//bağlantılı listeyi gözden geçirin
    while (cursor != NULL)
    {
        //kelimenin eşleşip eşleşmediğini kontrol edin
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
//imleci sonraki düğüme taşı
        cursor = cursor->next;
    }

    return false;
}

// Sözlüğü bellekten kaldırır, başarılı olrsa true değilse false döndürür
bool unload(void)
{
    // Hash Kovaları boyunca yineleme
    for (int i = 0; i < N; i++)
    {
        // Her hash kovası için cursor'u ayarlar  
        node *cursor = hashtable[i];
   
   while (cursor != NULL)
   {
       node *temp = cursor;
       cursor = cursor ->next;
       free (temp);
   }
   // Eğer cursor NULL ise
        if (i == N - 1 && cursor == NULL)
        {
            return true;
        }
    }
    return false;
}