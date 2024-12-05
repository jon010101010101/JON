#include <stdio.h>
#include <fcntl.h>	
#include "get_next_line.h"

#define GREEN "\033[0;32m"
#define RESET "\033[0m"

int main(void)
{
   int i;
   char *line;

	i = 1;
	
	while (i <= 3)
	{
		printf(GREEN "escribe la linea %d\n" RESET, i);
		line = get_next_line(1);
		printf("linea (%d)  \n", i);
	    printf("%s\n", line);
		i++;
	} 
	printf("\n\n");
    return (0);
}
