#include <unistd.h>

#define SU argv[1][i]

int main(int argc, char **argv)
{
    if(argc == 2)
    {
        int i = 0;

        while(SU == 32 || SU == 9)
            i++;
        while(SU >= 33 && SU <= 126)
        {
            write(1, &SU, 1);
            i++;
        }
    }
    write(1, "\n", 1);
    return(0);
}