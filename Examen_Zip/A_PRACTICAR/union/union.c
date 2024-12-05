#include <unistd.h>

#define SU argv[1][i]
#define SU2 argv[2][j]

int main(int argc, char **argv)
{
    if(argc != 3)
    {
        write(1, "\n", 1);
        return(0);
    }

    int i = 0;
    int j;
    char seen[256]={0};

    while(SU)
    {
        if(!seen[(unsigned char)SU])
        {
            seen[(unsigned char)SU]= 1;
            write(1, &SU, 1);
        }
        i++;
    }
    while(SU2)
    {
        if(!seen[(unsigned char)SU2])
        {
            seen[(unsigned char)SU2]= 1;
            write(1, &SU2, 1);
        }
        j++;
    }
    write(1, "\n", 1);
    return(0);
}