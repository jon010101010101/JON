#include <unistd.h>
#include <stdio.h>

#define SU argv[1][i]

int main(int argc, char **argv)
{
    int i = 0;
    int j = 0;

    if (argc == 2)
    {
        while(SU == 32 || SU == 9)
            i++;
        while(SU)
        {
            if(SU == 32 || SU == 9)
                j=1;
            if (!(SU == 32 || SU == 9))
            {
                if(j)
                    write(1, "   ", 3);
                j = 0;
                    write(1, &SU, 1);
            }
            i++;
        }
    }
    write(1, "\n", 1);
    return(0);
}
