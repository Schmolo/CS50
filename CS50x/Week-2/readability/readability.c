#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text, int lenght);
int count_words(string text, int lenght);
int count_sentences(string text, int lenght);

int main(void)
{
    string text = get_string("Text: ");
    int lenght = strlen(text);
    int letters = count_letters(text, lenght);
    int words = count_words(text, lenght);
    int sentences = count_sentences(text, lenght);

    float l = 100.00 * letters / words;
    float s = 100.00 * sentences / words;
    //cli formula
    float index = 0.0588 * l - 0.296 * s - 15.8;
    int cli = round(index);

    if (cli < 1)
    {
        printf("Before Grade 1\n");
    }
    if (cli > 1 && cli < 16)
    {
        printf("Grade %i\n", cli);
    }
    if (cli > 15)
    {
        printf("Grade 16+\n");
    }
}

int count_letters(string text, int lenght)
{
    // create counter var to count the number of letters
    int counter = 0;
    // loop for the lenght of the user given text, if an char is Uppercase, convert to lower, then if char is between a and z increase the counter by one
    for (int i = 0; i < lenght; i++)
    {
        char lower = tolower(text[i]);

        if (lower >= 'a' && lower <= 'z')
        {
            counter++;
        }
    }
    return counter;
}

int count_words(string text, int lenght)
{
    // create counter var to count the number of words (plus one because there is no space after the last sentence)
    int counter = 1;
    // loop for the lenght of the user given text, if a char is an space, increase the counter by one to geth the number of words
    for (int i = 0; i < lenght; i++)
    {
        if (text[i] == ' ')
        {
            counter++;
        }
    }
    return counter;
}

int count_sentences(string text, int lenght)
{
    // create counter var to count the number of sentences
    int counter = 0;
    // loop for the lenght of the user given text, if '!', '.' or '?' if so increase counter by one, to count number of sentences(sloppy)
    for (int i = 0; i < lenght; i++)
    {
        if (text[i] == '!' || text[i] == '.' || text[i] == '?')
        {
            counter++;
        }
    }
    return counter;
}