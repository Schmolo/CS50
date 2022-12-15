#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size;
    while (true)
    {
        size = get_int("Pyramid size(1-8): ");
        if (size <= 8 && size >= 1)
        {
            break;
        }
    }
    int s = size - 1;
    int hash = 1;
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < s; j++)
        {
            printf(" ");
        }
        s--;
        for (int l = 0; l < hash; l++)
        {
            printf("#");
        }
        hash++;
        printf("\n");
    }

}