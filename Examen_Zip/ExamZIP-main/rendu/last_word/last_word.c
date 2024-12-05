#include <unistd.h>

#define SU_M argv[1][i-1]

int main(int argc, char **argv)
{
    if(argc == 2)
    {
        int i = 0;
        int start = 0;
        int end = 0;

        while(argv[1][i])
            i++;
        while(SU_M == 32 || SU_M == 9)
            i--;
        end = i;
        while(SU_M >= 33 && SU_M <= 126)
            i--;
        start = i;
        while(start < end)
            write(1, &argv[1][start++], 1);
    }
    write(1, "\n", 1);
    return(0);
}