#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char UPPERCASE[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
char LOWERCASE[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

bool only_digits(string input);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // if more than one argument given close
    if (argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // if no argument given close
    if (argc < 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // if given argument contains non digit caracters close
    if (only_digits(argv[1]) == 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // get Plaintext input
    string plaintext = get_string("Plaintext: ");

    // convert string to int
    int input = atoi(argv[1]);
    // get lenght of plaintext input
    int lenght = strlen(plaintext);

    // pre print ciphertext
    printf("ciphertext: ");

    //print every single cipher text letter by letter
    for (int i = 0; i < lenght; i++)
    {
        printf("%c", rotate(plaintext[i], input));

    }
    printf("\n");
}

bool only_digits(string input)
{
    // get lenght of key and create counter var
    int lenght = strlen(input);
    int counter = 0;

    // check every character if digit and then increase counter
    for (int i = 0; lenght > i; i++)
    {
        if (input[i] >= '0' && input[i] <= '9')
        {
            counter++;
        }
    }
    // if number of character equals number of digits return true else false
    if (counter == lenght)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

char rotate(char c, int n)
{
    // check if given character is alphabetical else return the character
    if (isalpha(c))
    {
        // check if character is upper or lower case
        // then reduce it by its ascii number and use Caesar formula and return the result
        if (isupper(c))
        {
            int upper = c;
            upper -= 65;
            int upremainder = (upper + n) % 26;
            return UPPERCASE[upremainder];
        }
        else
        {
            int lower = c;
            lower -= 97;
            int loremainder = (lower + n) % 26;
            return LOWERCASE[loremainder];
        }
    }
    else
    {
        return c;
    }
}