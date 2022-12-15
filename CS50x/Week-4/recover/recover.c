#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    //if no target file given or too mutch info given print how to use
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //if opent file contains nothing or is not able to open print error
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }
    //initialize output var with NULL for later use
    FILE *output = NULL;

    int jpgcounter = 0;
    char output_name[8];

    BYTE buffer[BLOCK_SIZE];
    //loop through the blocks of the card.raw
    while (fread(&buffer, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
    {
        //if jpg identefier found generate the correct name, open a file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(output_name, "%03i.jpg", jpgcounter);

            output = fopen(output_name, "w");

            jpgcounter++;
        }
        //if output file is an initialize file so not NULL write to it
        if (output != NULL)
        {
            fwrite(buffer, sizeof(char), BLOCK_SIZE, output);
        }
    }
    //close everything opend before
    fclose(input);
    fclose(output);
}
