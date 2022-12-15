#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    if (score1 > score2)
    {
        printf("Player 1 Wins!\n");
    }
    if (score1 < score2)
    {
        printf("Player 2 Wins!\n");
    }
    if (score1 == score2)
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // get lenght of string and create counter var
    int lenght = strlen(word);
    int counter = 0;

    // loop for lenght of word
    for (int i = 0; i < lenght; i++)
    {
        // force all letters to lowercase
        char lower = tolower(word[i]);

        // ignore everything thats not a-z
        if (lower >= 'a' && lower <= 'z')
        {
            // convert char to int
            int ascii = lower;
            // subtract -97 to get the number per letter (a = 0, b = 1)
            int ascii2 = ascii - 97;
            // give the right amount of points via the array
            counter += POINTS[ascii2];
        }
    }
    return counter;
}
