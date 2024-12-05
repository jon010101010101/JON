#include <unistd.h>

#define SU argv[1][i]

int main(int argc, char **argv)
{
    if(argc == 2)
    {
        int i = 0;

        while(SU)
        {
            if((SU >= 'a' && SU <= 'm') || (SU >= 'A' && SU <= 'M'))
                SU = SU + 13;
            else if((SU >= 'n' && SU <= 'z') || (SU >= 'N' && SU <= 'Z'))
                SU = SU - 13;
            write(1, &SU, 1);
            i++;
        }
    }
    write( 1, "\n", 1);
    return(0);
}