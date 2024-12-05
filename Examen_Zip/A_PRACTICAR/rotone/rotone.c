#include <unistd.h>

#define SU argv[1][i]

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int i = 0;

        while(SU)
        {
            if((SU >= 'a' && SU < 'z') || (SU >= 'A' && SU < 'Z'))
                SU = SU + 1;
            else if(SU == 'z')
                SU = 'a';
            else if(SU == 'Z')
                SU = 'A';    
            write(1, &SU, 1);
            i++;
        }
    }
    write(1, "\n", 1);
    return(0);
}