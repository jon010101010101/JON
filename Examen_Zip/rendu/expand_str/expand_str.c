#include <unistd.h>

#define SU argv[1][i]

int main(int argc, char **argv)
{
    if(argc == 2)
    {
        int i = 0;
        int j = 0;

        while(SU == 32 || SU == 9)
            i++;
        while(SU)
        {
            if(SU == 32 || SU == 9)

            j = i;
            if(SU >= 33 && SU <= 126)
            {
                if(j)
                    write(1,"   ",3);
                j=0;
                    write(1,&SU,1);
            }
            i++;
            
        }
    }
    write( 1, "\n", 1);
    return(0);
}

