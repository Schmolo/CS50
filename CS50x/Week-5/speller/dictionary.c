// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Choose number of buckets in hash table
const unsigned int N = 17576;

// Hash table
node *table[N];

// Counter var for size function
int counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Index given word and check if word is in Linked List else return false
    int index = hash(word);
    for (node *tmp = table[index]; tmp != NULL; tmp = tmp->next)
    {
        if (strcasecmp(tmp->word, word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Checks first 2 Letters and gives an Hash Index depending on lenght
    if (strlen(word) > 2)
    {
        return ((toupper(word[0]) - 'A') * 676) + ((toupper(word[1]) - 'A') * 26) + (toupper(word[2]) - 'A');
    }
    if (strlen(word) > 1)
    {
        return ((toupper(word[0]) - 'A') * 26) + (toupper(word[1]) - 'A');
    }
    else
    {
        return toupper(word[0]) - 'A';
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open Dictionary
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];
    // Loop trough the Dictionary. Index every word and put it in an Hash Table
    while ((fscanf(input, "%s", buffer)) != EOF)
    {
        node *tmp = malloc(sizeof(node));
        if (tmp == NULL)
        {
            return false;
        }
        int index = hash(buffer);
        strcpy(tmp->word, buffer);

        tmp->next = table[index];

        table[index] = tmp;
        // Counter var for size function
        counter++;
    }
    fclose(input);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Return counter var, wich gets increased everytime a word gets loaded from an Dictionary
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Loop throug every list top to bottom
    for (int i = 0; i < N; i++)
    {
        // Loop through a list and free every node one by one
        node *tmp = NULL;
        for (node *cursor = table[i]; cursor != NULL; cursor = tmp)
        {
            tmp = cursor->next;

            free(cursor);

        }
        free(tmp);
    }
    return true;
}
